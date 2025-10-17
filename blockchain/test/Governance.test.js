/**
 * International Plebeian Academy - Governance Smart Contract Tests
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

const Governance = artifacts.require("Governance");
const TribalCoin = artifacts.require("TribalCoin");

contract("Governance", (accounts) => {
  let governance;
  let tribalCoin;
  const owner = accounts[0];
  const voter1 = accounts[1];
  const voter2 = accounts[2];
  const initialSupply = web3.utils.toWei("1000000", "ether");

  beforeEach(async () => {
    tribalCoin = await TribalCoin.new(initialSupply, { from: owner });
    governance = await Governance.new(tribalCoin.address, { from: owner });
    
    await tribalCoin.transfer(voter1, web3.utils.toWei("1000", "ether"), { from: owner });
    await tribalCoin.transfer(voter2, web3.utils.toWei("1000", "ether"), { from: owner });
  });

  describe("Proposal Creation", () => {
    it("should create a new proposal", async () => {
      const description = "Test proposal";
      const votingPeriod = 7 * 24 * 60 * 60;
      
      const result = await governance.createProposal(description, votingPeriod, { from: owner });
      
      assert.equal(result.logs.length, 1, "Should emit one event");
      assert.equal(result.logs[0].event, "ProposalCreated", "Should emit ProposalCreated event");
    });

    it("should increment proposal count", async () => {
      const description = "Test proposal";
      const votingPeriod = 7 * 24 * 60 * 60;
      
      await governance.createProposal(description, votingPeriod, { from: owner });
      const proposalCount = await governance.proposalCount();
      
      assert.equal(proposalCount.toNumber(), 1, "Proposal count should be 1");
    });
  });

  describe("Voting", () => {
    let proposalId;

    beforeEach(async () => {
      const description = "Test proposal";
      const votingPeriod = 7 * 24 * 60 * 60;
      const result = await governance.createProposal(description, votingPeriod, { from: owner });
      proposalId = result.logs[0].args.proposalId.toNumber();
    });

    it("should allow voting on proposal", async () => {
      const result = await governance.vote(proposalId, true, { from: voter1 });
      
      assert.equal(result.logs.length, 1, "Should emit one event");
      assert.equal(result.logs[0].event, "VoteCast", "Should emit VoteCast event");
    });

    it("should not allow voting twice", async () => {
      await governance.vote(proposalId, true, { from: voter1 });
      
      try {
        await governance.vote(proposalId, true, { from: voter1 });
        assert.fail("Should not allow double voting");
      } catch (error) {
        assert.include(error.message, "revert", "Should revert on double voting");
      }
    });

    it("should count votes correctly", async () => {
      await governance.vote(proposalId, true, { from: voter1 });
      await governance.vote(proposalId, true, { from: voter2 });
      
      const proposal = await governance.proposals(proposalId);
      assert.equal(proposal.votesFor.toNumber(), 2, "Should have 2 votes for");
    });
  });

  describe("Proposal Execution", () => {
    let proposalId;

    beforeEach(async () => {
      const description = "Test proposal";
      const votingPeriod = 1;
      const result = await governance.createProposal(description, votingPeriod, { from: owner });
      proposalId = result.logs[0].args.proposalId.toNumber();
    });

    it("should execute proposal after voting period", async () => {
      await governance.vote(proposalId, true, { from: voter1 });
      
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      const result = await governance.executeProposal(proposalId, { from: owner });
      
      assert.equal(result.logs[0].event, "ProposalExecuted", "Should emit ProposalExecuted event");
    });
  });
});

/**
 * International Plebeian Academy - TribalCoin Smart Contract Tests
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

const TribalCoin = artifacts.require("TribalCoin");

contract("TribalCoin", (accounts) => {
  let tribalCoin;
  const owner = accounts[0];
  const recipient = accounts[1];
  const initialSupply = web3.utils.toWei("1000000", "ether");

  beforeEach(async () => {
    tribalCoin = await TribalCoin.new(initialSupply, { from: owner });
  });

  describe("Deployment", () => {
    it("should deploy with correct initial supply", async () => {
      const totalSupply = await tribalCoin.totalSupply();
      assert.equal(
        totalSupply.toString(),
        initialSupply,
        "Initial supply should match"
      );
    });

    it("should assign total supply to owner", async () => {
      const ownerBalance = await tribalCoin.balanceOf(owner);
      assert.equal(
        ownerBalance.toString(),
        initialSupply,
        "Owner should have total supply"
      );
    });

    it("should have correct name and symbol", async () => {
      const name = await tribalCoin.name();
      const symbol = await tribalCoin.symbol();
      assert.equal(name, "TribalCoin", "Name should be TribalCoin");
      assert.equal(symbol, "TRIBAL", "Symbol should be TRIBAL");
    });
  });

  describe("Transfers", () => {
    it("should transfer tokens between accounts", async () => {
      const amount = web3.utils.toWei("100", "ether");
      
      await tribalCoin.transfer(recipient, amount, { from: owner });
      
      const recipientBalance = await tribalCoin.balanceOf(recipient);
      assert.equal(
        recipientBalance.toString(),
        amount,
        "Recipient should receive tokens"
      );
    });

    it("should fail when sender has insufficient balance", async () => {
      const amount = web3.utils.toWei("1000000", "ether");
      
      try {
        await tribalCoin.transfer(owner, amount, { from: recipient });
        assert.fail("Transfer should have thrown an error");
      } catch (error) {
        assert.include(
          error.message,
          "revert",
          "Should revert with insufficient balance"
        );
      }
    });
  });

  describe("Allowances", () => {
    it("should approve spending allowance", async () => {
      const amount = web3.utils.toWei("50", "ether");
      
      await tribalCoin.approve(recipient, amount, { from: owner });
      
      const allowance = await tribalCoin.allowance(owner, recipient);
      assert.equal(
        allowance.toString(),
        amount,
        "Allowance should be set correctly"
      );
    });

    it("should transfer from approved allowance", async () => {
      const amount = web3.utils.toWei("50", "ether");
      
      await tribalCoin.approve(recipient, amount, { from: owner });
      await tribalCoin.transferFrom(owner, recipient, amount, { from: recipient });
      
      const recipientBalance = await tribalCoin.balanceOf(recipient);
      assert.equal(
        recipientBalance.toString(),
        amount,
        "Recipient should receive tokens from allowance"
      );
    });
  });
});

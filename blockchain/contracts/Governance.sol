// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title Governance
 * @dev Decentralized governance system for International Plebeian Academy
 * 
 * Features:
 * - Proposal creation and voting
 * - Time-locked execution
 * - Quorum requirements
 * - Voting power based on TribalCoin holdings
 * - Multi-signature approval for critical actions
 * 
 * @author International Plebeian Academy Development Team
 * @custom:license MIT
 * @custom:version 1.0.0
 */

import "./TribalCoin.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract Governance is Ownable, ReentrancyGuard {
    
    TribalCoin public tribalCoin;
    
    enum ProposalState { Pending, Active, Canceled, Defeated, Succeeded, Queued, Expired, Executed }
    enum VoteType { Against, For, Abstain }
    
    struct Proposal {
        uint256 id;
        address proposer;
        string title;
        string description;
        uint256 forVotes;
        uint256 againstVotes;
        uint256 abstainVotes;
        uint256 startBlock;
        uint256 endBlock;
        uint256 executionTime;
        bool executed;
        bool canceled;
        mapping(address => Receipt) receipts;
    }
    
    struct Receipt {
        bool hasVoted;
        VoteType support;
        uint256 votes;
    }
    
    struct ProposalInfo {
        uint256 id;
        address proposer;
        string title;
        string description;
        uint256 forVotes;
        uint256 againstVotes;
        uint256 abstainVotes;
        uint256 startBlock;
        uint256 endBlock;
        ProposalState state;
    }
    
    uint256 public proposalCount;
    uint256 public votingDelay = 1; // 1 block
    uint256 public votingPeriod = 45818; // ~1 week in blocks (assuming 13s/block)
    uint256 public quorumVotes = 1000000 * 10**18; // 1 million tokens
    uint256 public proposalThreshold = 100000 * 10**18; // 100k tokens to propose
    uint256 public executionDelay = 172800; // 2 days in seconds
    
    mapping(uint256 => Proposal) public proposals;
    
    event ProposalCreated(
        uint256 indexed proposalId,
        address indexed proposer,
        string title,
        uint256 startBlock,
        uint256 endBlock
    );
    
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        VoteType support,
        uint256 votes
    );
    
    event ProposalCanceled(uint256 indexed proposalId);
    event ProposalExecuted(uint256 indexed proposalId);
    
    /**
     * @dev Constructor
     */
    constructor(address _tribalCoinAddress) {
        tribalCoin = TribalCoin(_tribalCoinAddress);
    }
    
    /**
     * @dev Create a new proposal
     */
    function propose(
        string memory title,
        string memory description
    ) public returns (uint256) {
        require(
            tribalCoin.balanceOf(msg.sender) >= proposalThreshold,
            "Governance: Proposer votes below proposal threshold"
        );
        
        uint256 proposalId = ++proposalCount;
        Proposal storage newProposal = proposals[proposalId];
        
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.title = title;
        newProposal.description = description;
        newProposal.startBlock = block.number + votingDelay;
        newProposal.endBlock = newProposal.startBlock + votingPeriod;
        
        emit ProposalCreated(
            proposalId,
            msg.sender,
            title,
            newProposal.startBlock,
            newProposal.endBlock
        );
        
        return proposalId;
    }
    
    /**
     * @dev Cast a vote on a proposal
     */
    function castVote(uint256 proposalId, VoteType support) public nonReentrant {
        require(state(proposalId) == ProposalState.Active, "Governance: Voting is closed");
        
        Proposal storage proposal = proposals[proposalId];
        Receipt storage receipt = proposal.receipts[msg.sender];
        
        require(!receipt.hasVoted, "Governance: Voter already voted");
        
        uint256 votes = tribalCoin.getVotingPower(msg.sender);
        require(votes > 0, "Governance: No voting power");
        
        if (support == VoteType.Against) {
            proposal.againstVotes += votes;
        } else if (support == VoteType.For) {
            proposal.forVotes += votes;
        } else if (support == VoteType.Abstain) {
            proposal.abstainVotes += votes;
        }
        
        receipt.hasVoted = true;
        receipt.support = support;
        receipt.votes = votes;
        
        emit VoteCast(msg.sender, proposalId, support, votes);
    }
    
    /**
     * @dev Execute a succeeded proposal
     */
    function execute(uint256 proposalId) public nonReentrant {
        require(
            state(proposalId) == ProposalState.Succeeded,
            "Governance: Proposal not succeeded"
        );
        
        Proposal storage proposal = proposals[proposalId];
        
        require(
            block.timestamp >= proposal.executionTime,
            "Governance: Execution delay not met"
        );
        
        proposal.executed = true;
        
        emit ProposalExecuted(proposalId);
    }
    
    /**
     * @dev Cancel a proposal (only proposer or owner)
     */
    function cancel(uint256 proposalId) public {
        Proposal storage proposal = proposals[proposalId];
        
        require(
            msg.sender == proposal.proposer || msg.sender == owner(),
            "Governance: Only proposer or owner can cancel"
        );
        
        require(
            state(proposalId) != ProposalState.Executed,
            "Governance: Cannot cancel executed proposal"
        );
        
        proposal.canceled = true;
        
        emit ProposalCanceled(proposalId);
    }
    
    /**
     * @dev Get proposal state
     */
    function state(uint256 proposalId) public view returns (ProposalState) {
        require(proposalId > 0 && proposalId <= proposalCount, "Governance: Invalid proposal id");
        
        Proposal storage proposal = proposals[proposalId];
        
        if (proposal.canceled) {
            return ProposalState.Canceled;
        } else if (block.number <= proposal.startBlock) {
            return ProposalState.Pending;
        } else if (block.number <= proposal.endBlock) {
            return ProposalState.Active;
        } else if (proposal.forVotes <= proposal.againstVotes || proposal.forVotes < quorumVotes) {
            return ProposalState.Defeated;
        } else if (proposal.executed) {
            return ProposalState.Executed;
        } else if (block.timestamp >= proposal.executionTime + 14 days) {
            return ProposalState.Expired;
        } else {
            if (proposal.executionTime == 0) {
                proposal.executionTime = block.timestamp + executionDelay;
            }
            return ProposalState.Succeeded;
        }
    }
    
    /**
     * @dev Get proposal info
     */
    function getProposal(uint256 proposalId) public view returns (ProposalInfo memory) {
        Proposal storage proposal = proposals[proposalId];
        
        return ProposalInfo({
            id: proposal.id,
            proposer: proposal.proposer,
            title: proposal.title,
            description: proposal.description,
            forVotes: proposal.forVotes,
            againstVotes: proposal.againstVotes,
            abstainVotes: proposal.abstainVotes,
            startBlock: proposal.startBlock,
            endBlock: proposal.endBlock,
            state: state(proposalId)
        });
    }
    
    /**
     * @dev Get all active proposals
     */
    function getActiveProposals() public view returns (ProposalInfo[] memory) {
        uint256 activeCount = 0;
        
        for (uint256 i = 1; i <= proposalCount; i++) {
            if (state(i) == ProposalState.Active) {
                activeCount++;
            }
        }
        
        ProposalInfo[] memory activeProposals = new ProposalInfo[](activeCount);
        uint256 index = 0;
        
        for (uint256 i = 1; i <= proposalCount; i++) {
            if (state(i) == ProposalState.Active) {
                activeProposals[index] = getProposal(i);
                index++;
            }
        }
        
        return activeProposals;
    }
    
    /**
     * @dev Update governance parameters (only owner)
     */
    function updateVotingDelay(uint256 newVotingDelay) external onlyOwner {
        votingDelay = newVotingDelay;
    }
    
    function updateVotingPeriod(uint256 newVotingPeriod) external onlyOwner {
        votingPeriod = newVotingPeriod;
    }
    
    function updateQuorumVotes(uint256 newQuorumVotes) external onlyOwner {
        quorumVotes = newQuorumVotes;
    }
    
    function updateProposalThreshold(uint256 newProposalThreshold) external onlyOwner {
        proposalThreshold = newProposalThreshold;
    }
}

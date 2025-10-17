// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title TribalCoin
 * @dev ERC20 token for International Plebeian Academy
 * 
 * Features:
 * - Standard ERC20 functionality
 * - Minting controlled by governance
 * - Burning mechanism
 * - Transfer restrictions for compliance
 * - Voting power based on token holdings
 * 
 * @author International Plebeian Academy Development Team
 * @custom:license MIT
 * @custom:version 1.0.0
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract TribalCoin is ERC20, ERC20Burnable, AccessControl, Pausable {
    
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    bytes32 public constant GOVERNANCE_ROLE = keccak256("GOVERNANCE_ROLE");
    
    uint256 public constant MAX_SUPPLY = 1000000000 * 10**18; // 1 billion tokens
    uint256 public constant INITIAL_SUPPLY = 100000000 * 10**18; // 100 million tokens
    
    mapping(address => bool) public blacklisted;
    
    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);
    event AddressBlacklisted(address indexed account);
    event AddressWhitelisted(address indexed account);
    
    /**
     * @dev Constructor that gives msg.sender all existing tokens.
     */
    constructor() ERC20("TribalCoin", "TRIBAL") {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(MINTER_ROLE, msg.sender);
        _setupRole(PAUSER_ROLE, msg.sender);
        _setupRole(GOVERNANCE_ROLE, msg.sender);
        
        _mint(msg.sender, INITIAL_SUPPLY);
    }
    
    /**
     * @dev Mint new tokens (only MINTER_ROLE)
     */
    function mint(address to, uint256 amount) public onlyRole(MINTER_ROLE) {
        require(totalSupply() + amount <= MAX_SUPPLY, "TribalCoin: Max supply exceeded");
        require(!blacklisted[to], "TribalCoin: Recipient is blacklisted");
        
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }
    
    /**
     * @dev Pause token transfers (only PAUSER_ROLE)
     */
    function pause() public onlyRole(PAUSER_ROLE) {
        _pause();
    }
    
    /**
     * @dev Unpause token transfers (only PAUSER_ROLE)
     */
    function unpause() public onlyRole(PAUSER_ROLE) {
        _unpause();
    }
    
    /**
     * @dev Blacklist an address (only GOVERNANCE_ROLE)
     */
    function blacklistAddress(address account) public onlyRole(GOVERNANCE_ROLE) {
        require(!blacklisted[account], "TribalCoin: Address already blacklisted");
        blacklisted[account] = true;
        emit AddressBlacklisted(account);
    }
    
    /**
     * @dev Remove address from blacklist (only GOVERNANCE_ROLE)
     */
    function whitelistAddress(address account) public onlyRole(GOVERNANCE_ROLE) {
        require(blacklisted[account], "TribalCoin: Address not blacklisted");
        blacklisted[account] = false;
        emit AddressWhitelisted(account);
    }
    
    /**
     * @dev Get voting power for an address
     */
    function getVotingPower(address account) public view returns (uint256) {
        return balanceOf(account);
    }
    
    /**
     * @dev Override transfer to add blacklist and pause checks
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        require(!blacklisted[from], "TribalCoin: Sender is blacklisted");
        require(!blacklisted[to], "TribalCoin: Recipient is blacklisted");
        super._beforeTokenTransfer(from, to, amount);
    }
}

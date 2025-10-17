// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title FileVerification
 * @dev Blockchain-based file integrity verification system
 * 
 * Features:
 * - File hash storage on blockchain
 * - Timestamp verification
 * - Ownership tracking
 * - Verification history
 * - Multi-signature validation
 * 
 * @author International Plebeian Academy Development Team
 * @custom:license MIT
 * @custom:version 1.0.0
 */

import "@openzeppelin/contracts/access/Ownable.sol";

contract FileVerification is Ownable {
    
    struct FileRecord {
        bytes32 fileHash;
        address uploader;
        uint256 timestamp;
        string fileName;
        string fileType;
        uint256 fileSize;
        bool exists;
        mapping(address => bool) verifiers;
        uint256 verificationCount;
    }
    
    struct FileInfo {
        bytes32 fileHash;
        address uploader;
        uint256 timestamp;
        string fileName;
        string fileType;
        uint256 fileSize;
        uint256 verificationCount;
    }
    
    mapping(bytes32 => FileRecord) public files;
    mapping(address => bytes32[]) public userFiles;
    
    bytes32[] public allFileHashes;
    
    event FileRegistered(
        bytes32 indexed fileHash,
        address indexed uploader,
        string fileName,
        uint256 timestamp
    );
    
    event FileVerified(
        bytes32 indexed fileHash,
        address indexed verifier,
        uint256 timestamp
    );
    
    /**
     * @dev Register a new file
     */
    function registerFile(
        bytes32 fileHash,
        string memory fileName,
        string memory fileType,
        uint256 fileSize
    ) public {
        require(!files[fileHash].exists, "FileVerification: File already registered");
        require(fileHash != bytes32(0), "FileVerification: Invalid file hash");
        
        FileRecord storage newFile = files[fileHash];
        newFile.fileHash = fileHash;
        newFile.uploader = msg.sender;
        newFile.timestamp = block.timestamp;
        newFile.fileName = fileName;
        newFile.fileType = fileType;
        newFile.fileSize = fileSize;
        newFile.exists = true;
        newFile.verificationCount = 0;
        
        userFiles[msg.sender].push(fileHash);
        allFileHashes.push(fileHash);
        
        emit FileRegistered(fileHash, msg.sender, fileName, block.timestamp);
    }
    
    /**
     * @dev Verify a file (add verification signature)
     */
    function verifyFile(bytes32 fileHash) public {
        require(files[fileHash].exists, "FileVerification: File not registered");
        require(!files[fileHash].verifiers[msg.sender], "FileVerification: Already verified by sender");
        
        FileRecord storage file = files[fileHash];
        file.verifiers[msg.sender] = true;
        file.verificationCount++;
        
        emit FileVerified(fileHash, msg.sender, block.timestamp);
    }
    
    /**
     * @dev Check if file exists
     */
    function fileExists(bytes32 fileHash) public view returns (bool) {
        return files[fileHash].exists;
    }
    
    /**
     * @dev Get file information
     */
    function getFileInfo(bytes32 fileHash) public view returns (FileInfo memory) {
        require(files[fileHash].exists, "FileVerification: File not registered");
        
        FileRecord storage file = files[fileHash];
        
        return FileInfo({
            fileHash: file.fileHash,
            uploader: file.uploader,
            timestamp: file.timestamp,
            fileName: file.fileName,
            fileType: file.fileType,
            fileSize: file.fileSize,
            verificationCount: file.verificationCount
        });
    }
    
    /**
     * @dev Check if address has verified a file
     */
    function hasVerified(bytes32 fileHash, address verifier) public view returns (bool) {
        require(files[fileHash].exists, "FileVerification: File not registered");
        return files[fileHash].verifiers[verifier];
    }
    
    /**
     * @dev Get all files uploaded by a user
     */
    function getUserFiles(address user) public view returns (bytes32[] memory) {
        return userFiles[user];
    }
    
    /**
     * @dev Get total number of registered files
     */
    function getTotalFiles() public view returns (uint256) {
        return allFileHashes.length;
    }
    
    /**
     * @dev Get all registered file hashes
     */
    function getAllFileHashes() public view returns (bytes32[] memory) {
        return allFileHashes;
    }
    
    /**
     * @dev Verify file integrity by comparing hash
     */
    function verifyIntegrity(
        bytes32 fileHash,
        bytes32 providedHash
    ) public view returns (bool) {
        require(files[fileHash].exists, "FileVerification: File not registered");
        return fileHash == providedHash;
    }
    
    /**
     * @dev Get file timestamp
     */
    function getFileTimestamp(bytes32 fileHash) public view returns (uint256) {
        require(files[fileHash].exists, "FileVerification: File not registered");
        return files[fileHash].timestamp;
    }
    
    /**
     * @dev Get file uploader
     */
    function getFileUploader(bytes32 fileHash) public view returns (address) {
        require(files[fileHash].exists, "FileVerification: File not registered");
        return files[fileHash].uploader;
    }
}

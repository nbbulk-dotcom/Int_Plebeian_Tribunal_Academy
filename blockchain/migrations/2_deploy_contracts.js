/**
 * International Plebeian Academy - Contract Deployment Migration
 * 
 * Deploys all smart contracts in correct order:
 * 1. TribalCoin (ERC20 token)
 * 2. Governance (with TribalCoin address)
 * 3. FileVerification
 * 
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

const TribalCoin = artifacts.require("TribalCoin");
const Governance = artifacts.require("Governance");
const FileVerification = artifacts.require("FileVerification");

module.exports = async function (deployer, network, accounts) {
  
  await deployer.deploy(TribalCoin);
  const tribalCoin = await TribalCoin.deployed();
  console.log("TribalCoin deployed at:", tribalCoin.address);
  
  await deployer.deploy(Governance, tribalCoin.address);
  const governance = await Governance.deployed();
  console.log("Governance deployed at:", governance.address);
  
  await deployer.deploy(FileVerification);
  const fileVerification = await FileVerification.deployed();
  console.log("FileVerification deployed at:", fileVerification.address);
  
  const GOVERNANCE_ROLE = await tribalCoin.GOVERNANCE_ROLE();
  await tribalCoin.grantRole(GOVERNANCE_ROLE, governance.address);
  console.log("Granted GOVERNANCE_ROLE to Governance contract");
  
  console.log("\nDeployment Summary:");
  console.log("===================");
  console.log("Network:", network);
  console.log("Deployer:", accounts[0]);
  console.log("TribalCoin:", tribalCoin.address);
  console.log("Governance:", governance.address);
  console.log("FileVerification:", fileVerification.address);
};

/**
 * International Plebeian Academy - Initial Migration
 * 
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

const Migrations = artifacts.require("Migrations");

module.exports = function (deployer) {
  deployer.deploy(Migrations);
};

# EcoChallenge - EcoCode Rule Validator

The objective of this project is to provide a generic tool to facilitate the validation of new rules.

## Principles

For each potential rule, the rule validator will take as inputs :
  - a file containing the "good code"
  - a file containing the "bad code" (code smell)
  - a file containing the test scenarios to be executed.

  For each scenario, the rule validator will instrumente it with monitoring tools (actually only one - vjoule) and will generate some results file.

  You can find some generated sample files in the folder **/samples**. 

  Based on those results file, a graphic summary is generated for each rule.

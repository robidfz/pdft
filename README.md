# The Predictive Fault Tree Language

## Motivation

## Definition of the language

## Content of the repository


## Usage

### Validator
The following checks are performed on a parsed file:
* **dynamics**:
  * [x] the names of the dynamics are unique;
* **component**:
  * [ ] the names of the parameters are unique;
  * [ ] the names of the states are unique;
  * [ ] the names of the input ports are unique;
  * [ ] the names of the input ports are different from the output one;
  * [ ] the target of a transition is a state;
  * [ ] the source of a transition is a state;
  * [ ] in the trigger expression, only input ports and known dynamics can appear;
  * [ ] the weight of a transition is a number between 0 and 1;
  * [ ] the action of a transition is a value in {true, false, neutral}.
* **model**: 
  * [ ] the names of the parameters are unique;
  * [ ] the names of the dynamics are present in dynamics section;
  * [ ] the names of the component instances are unique;
  * [ ] the component of a component instance is in the list of the component;
  * [ ] the list of parameter bindings is of the same lenght of the component's parameter bindings;
  * [ ] each event starts from a component instance with a legal state;
  * [ ] each event ends to a component instance with a legal state;
  * [ ] the weight of an event is a number between 0 and 1;
  * [ ] the condition of the cost function involves objects and legal states;
  * [ ] the value of the cost function is a value or a model parameter.


## Requisites


## Contributors
* Stefano Marrone, Università della Campania "Luigi Vanvitelli"
* Roberta De Fazio, Università della Campania "Luigi Vanvitelli"



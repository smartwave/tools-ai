# ai-solution-builder-stage-0 Specification

> No baseline spec exists for the `ai-solution-builder` plugin in this
> repository; the plugin predates OpenSpec here. Everything below is ADDED.

## ADDED Requirements

### Requirement: Stage 0 has four steps and one document per step

Stage 0 of the pipeline SHALL consist of Frame, POC Brief, Build, and POC Summary,
in that order, producing the Ultralight Problem Brief, the POC Brief, a throwaway
POC with a change log, and the POC Summary. None of the three documents SHALL be
a governed record or carry a tier.

#### Scenario: A person arrives wanting a POC with no brief

- **WHEN** `ai-poc-builder` is invoked and no POC Brief exists
- **THEN** it asks whether an Ultralight Problem Brief exists and offers
  `ai-problem-framer` before framing the question itself

### Requirement: The person authors; the tool guides

In every Stage 0 skill and Gem, the substance of the problem statement, root
cause, future state, testable question, and recommendation SHALL come from the
person. The tool SHALL ask questions, offer structures and examples from other
domains, and sharpen the person's own text. It SHALL NOT produce a draft of the
person's content from a topic alone.

#### Scenario: Topic with no content

- **WHEN** the person gives a topic and no description
- **THEN** the tool replies with questions and no draft

### Requirement: The brief is written in three gated phases

The Ultralight Problem Brief SHALL carry a `phase` value of `problem`,
`root-cause`, `future-state`, or `complete`. The tool SHALL read it before acting
and SHALL act only in the phase it names. A confirmed section SHALL be read-only
in later phases; re-opening a phase SHALL be stated explicitly and the later
sections re-checked afterwards.

#### Scenario: Root-cause phase asked to change the problem statement

- **WHEN** `phase` is `root-cause` and the person asks to reword Section 1
- **THEN** the tool declines, names re-opening Phase 1 as the route, and does
  not edit Section 1

### Requirement: Root-cause phase never writes on its first response

On entering the root-cause phase, the tool's first response SHALL read Section 1
back verbatim, state that it is read-only, and ask the first "why". It SHALL NOT
output an updated brief in that response.

#### Scenario: First response in the root-cause phase

- **WHEN** the tool enters the root-cause phase
- **THEN** its first response contains no updated brief and exactly one question

### Requirement: Root cause is validated before it is written

The tool SHALL write Section 2 only after the person confirms the cause in their
own words and states how they know, or labels it suspected with a named
confirming check.

#### Scenario: No evidence

- **WHEN** the person cannot say how they know the cause
- **THEN** the cause is recorded as suspected with the confirming check as the
  first action, ahead of any POC

### Requirement: Future state is process-level and confirmed before writing

Section 3 SHALL describe the flow of work, hand-offs, and checks, SHALL NOT name
individuals as the problem or the fix, SHALL NOT name a product, and SHALL be
written only after the person confirms the exact text.

#### Scenario: Sentence names a person

- **WHEN** a proposed future-state sentence names an individual
- **THEN** the tool rewrites it to name the process step before confirming

### Requirement: The POC Brief carries the brief forward read-only and adds only build needs

`ai-poc-brief-author` SHALL refuse without a brief whose `phase` is `complete`,
SHALL copy the three sections verbatim into Section A, and SHALL tick the three
safety pre-flight boxes only on the person's explicit yes.

#### Scenario: Real data requested

- **WHEN** the person asks to use real customer data in the POC
- **THEN** the tool declines, offers synthetic data, and does not tick the
  pre-flight box

### Requirement: The POC build keeps a change log

`ai-poc-builder` SHALL record every change made while building — what changed,
why, who asked, effect on the answer — from the first change, in the format of
the POC Summary's change-log section.

#### Scenario: Small change

- **WHEN** a change is made that seems too small to note
- **THEN** it is still recorded

### Requirement: The POC Summary records only what happened

`ai-poc-summary-author` SHALL take every number and result from the person,
SHALL write "not measured" where none exists, SHALL mark an incomplete change
log as incomplete, SHALL tick tripwire boxes only on an explicit yes, and SHALL
NOT offer a recommendation before the person gives theirs.

#### Scenario: Un-tickable tripwire

- **WHEN** the POC has been used by someone other than the author
- **THEN** the summary says so and directs the person to stop using it and
  start Gate 1

### Requirement: Gemini parity

The `gems/` folder SHALL hold five Gem instruction sets producing the same five
outputs, each restating the governing rule at the top, inside each step, in a
pre-reply self-check, and at the end, and each reading the brief's `phase` line
before acting.

#### Scenario: Gem asked to act in the wrong phase

- **WHEN** the Root Cause Gem receives a brief whose `phase` is `problem`
- **THEN** it declines and points to the Problem Statement Gem

# PlayWBDD.Framework
Automation testing with python playwright and behave

## Overview
PlayWBDD.Framework is a framework for automating web application testing, combining the power of Playwright for browser interaction and the principles of behavior-driven testing (BDD) using Behave.

## Key Features
- Integration with Playwright for browser automation
- Support for BDD approach through Behave
- Built-in logging
- Test lifecycle management
- Tag support for flexible test execution management

## Managing Tests via Tags
The framework supports the following tags:
- @skip: Skip the test
- @wip: Test in progress (Work in Progress)
- @manual: Manual test

## Logging
The framework uses a built-in logging mechanism with the following levels:
- INFO: General information about execution
- SUCCESS: Successful execution of the scenario
- WARNING: Warnings (e.g., skipped tests)
- ERROR: Execution errors

## Steps

### Attribute Steps
 Given the "Some element" (is|is not|become|become not) (enabled|disabled)
 When the "Some element" (is|is not|become|become not) (enabled|disabled)
 Then the "Some element" should (be|be not|become|become not) (enabled|disabled)

 Given the "Some element" (is|is not|become|become not) (visible|invisible)
 When the "Some element" (is|is not|become|become not) (visible|invisible)
 Then the "Some element" should (be|be not|become|become not) (visible|invisible)

### Click Steps
 Given user clicked on "Test button"
 When user clicks on "Test button"

 Given user clicked twice on "Test button"
 When user clicks twice on "Test button"

 Given user hovered mouse over "Test button"
 When user hovers mouse over "Test button"

### Debug Steps
 Given wait "5" sec
 When wait "5" sec
 Then wait "5" sec

### Dropdown Steps
 Given dropdown "Some dropdown" has the following values
 Then dropdown "Some dropdown" should have the following values <br/>
 **   |value       | <br/>
 **   |First option|

 Given (partially|exactly): dropdown "Some dropdown" (contains|not contains) the following values
 Then (partially|exactly): dropdown "Some dropdown" (contains|not contains) the followingvalues <br/>
 **   |value       | <br/>
 **   |First option|

 Given the following values are selected in "Some dropdown"
 Then the following values should be selected in "Some dropdown" <br/>
 **   |value       | <br/>
 **   |First option|

 Given the following values {behavior} in "Some dropdown" dropdown
 Then the following values should be {behavior} in "Some dropdown" dropdown <br/>
 **   |value       | <br/>
 **   |First option|

 Given no values are selected in "Some dropdown"
 Then no values should be selected in "Some dropdown"

 Given deselected all values in "Some dropdown"
 When deselects all values in "Some dropdown"

 Given user selects values in "Some dropdown"
 When user selects values in "Some dropdown" <br/>
 **   |value       | <br/>
 **   |First option|

### Download Steps
 Then "{filename}" file should be downloaded

### Input Steps
 Given user entered "Some text/value" into "Input_name" input
 When user enters "Some text/value" into "Input_name" input

 Given user cleared "Input_name" input
 When user clears "Input_name" input

### Label Steps
 Given the element "Test-element" text (is|is not|become) "expected text"
 Then the element "Test-element" text should (be|be not|become not) "expected text"

 Given inside "Test-element" (contains|does not contains) "expected string" text
 Then inside "Test-element" should (contain|not contain) "expected string" text

 Given text (is|is not|become) empty inside "Test-element"
 Then text should (be|be not|become not) empty inside "Test-element"

### List steps
 Given list "Some list" (has|does not have) the following items <br/>
 **   |itemName     | <br/>
 **   |Test value 1 | <br/>
 **   |Test value 2 |
 Then list "Some list" (have|not have) the following items <br/>
 **   |itemName     | <br/>
 **   |Test value 1 | <br/>
 **   |Test value 2 |

 Given in exact order list "Some list" (has|does not have) the following items <br/>
 **   |itemName     | <br/>
 **   |Test value 1 | <br/>
 **   |Test value 2 |
 Then in exact order list "Some list" (have|not have) the following items <br/>
 **   |itemName     | <br/>
 **   |Test value 1 | <br/>
 **   |Test value 2 |

### Navigation steps
 Given URL is opened
 When user opens URL

 Given URL "https://example.com/" is opened
 When user opens URL "https://example.com/"

 Given relative URL "/test-url" is opened
 When user opens relative URL "/test-url"

 Given page URL "https://example.com/" (is|is not|becomes|becomes not) opened
 Then page URL "https://example.com/" should (be|not be|become|not become) opened

 Given relative URL (is|is not|become|become not) "/test-page"
 Then relative URL should (be|be not|become|become not) "/test-page"

 Given page (contains|not contains) "https://example.com/" URL
 Then page (should|should not) contain "https://example.com/" URL

 Given page title (is|is not|become|become not) "title"
 Then page title should (be|be not|become|become not) "title"

 Given user reloaded current page
 When user reloads current page

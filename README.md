# sublime-poor-mans-tsql-formatter

A Sublime Text plugin that runs the [poor-mans-t-sql-formatter-npm-cli](https://github.com/TaoK/poor-mans-t-sql-formatter-npm-cli) node library on the current file. poor-mans-t-sql-formatter-npm-cli is a command line interface for the [Poor Man's T-SQL Formatter](http://architectshack.com/PoorMansTSqlFormatter.ashx) tool.
This is my first Sublime plugin and this reason is very inspired by [sublime-sql-formatter](https://github.com/kufii/sublime-sql-formatter) project. I build this generally for my personal use, but feel free to use it.

## Installation

### Dependencies

This plugin requires node.js, and also requires poor-mans-t-sql-formatter-npm-cli to be globally installed.

`npm install -g poor-mans-t-sql-formatter-npm-cli`

### Plugin Installation

This plugin is installable via [Package Control](https://packagecontrol.io/installation)

To install via Package Control, do the following:

1. Within Sublime Text, bring up the Command Palette and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

2. When the plugin list appears, type `poor sql`. Among the entries you should see `poor-mans-tsql-formatter`. Select this entry to install it.

## Commands

### Command Palette

* `Poor Man's T-SQL Formatter: Format SQL`: Runs the formatter with the default settings.

### Default Hotkeys

By default, these hotkeys will run the formatter with the default dialect defined in your settings.

* Linux/Windows: [Ctrl + KQ]
* Mac: [Cmd + KQ]

## Settings

By default the following settings are used:

```javascript
{
	// The paths to look for executables
	"paths": {
		"linux": [],
		"osx": [],
		"windows": []
	},


	/**
	 * Standard formatter options
	 */

	// Use a specific character encoding supported by node for input - basically utf-16le or utf-8
	"inputEncoding": "utf-8",

	// Use a specific character encoding supported by node for input - basically utf-16le or utf-8
	"outputEncoding": "utf-8",

	// Add a byte order mark (BOM) to the start of the output
	"forceOutputBOM": false,

	// The unit of indentation - typically a tab (\t) or a number of spaces
	"indent": "\t",

	// Request that the formatter wrap long lines to avoid exceeding this line length
	"maxLineWidth": "999",

	// This is used to measure line length, and only applies if you use tabs
	"spacesPerTab": "4",

	// How many linebreaks should be added when starting a new statement?
	"statementBreaks": "2",

	// How many linebreaks should be added when starting a new clause within a statement?
	"clauseBreaks": "1",

	// Should comma-delimited lists (columns, group by args, etc) be broken out onto new lines?
	"no-expandCommaLists": false,

	// When starting a new line because of a comma, should the comma be at the end of line (VS the start of the next)?
	"no-trailingCommas": false,

	// Should a space be added after the comma? (typically not if they are "trailing")
	"spaceAfterExpandedComma": false,

	// Should boolean operators (AND, OR) cause a linebreak?
	"no-expandBooleanExpressions": false,

	// Should CASE expressions have their WHEN and THEN expressions be broken out on new lines?
	"no-expandCaseStatements": false,

	// Should BETWEEN expressions have the max argument broken out on a new line?
	"no-expandBetweenConditions": false,

	// Should IN() lists have each argument on a new line?
	"expandInLists": false,

	// Should the ON section of a JOIN clause be broken out onto its own line?
	"breakJoinOnSections": false,

	// Should T-SQL keywords (like SELECT, FROM) be automatically uppercased?
	"no-uppercaseKeywords": false,

	// Should less-common T-SQL keywords be replaced with their standard counterparts? (NOTE: only safe for T-SQL!)
	"keywordStandardization": false,

	/**
	 * Obfuscating formatter ("min" command) options
	 */

	 // Should the case of keywords be randomized, to minimize legibility?
	"randomizeKeywordCase": false,

	// Should the SQL be wrapped at arbitrary intervals, to minimize legibility?
	"randomizeLineLengths": false,

	// Should comments in the code be retained (vs being stripped out)?
	"no-preserveComments": false,

	// Should keywords with synonyms use less common forms? (NOTE: only safe for T-SQL!)
	"enableKeywordSubstitution": false
}
```

You can modify any settings by going to Preferences > Package Settings > Poor Man's T-SQL Formatter > Settings.


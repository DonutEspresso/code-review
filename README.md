code-review
===========

A python script and Sublime Text plugin used to parse review comments and outputs them, so you can attach them in email or use them as the contents of a bug report.

Review comments look like this in a file:

/* REVIEW:
/** REVIEW:
// REVIEW



CLI Version

The tool takes 3 arguments:
./codereview.py {filename} {author} {reviewer}

And outputs the parsed comments to a file.



Sublime Text Plugin

The plugin looks for two annotations in the file, "@author" and "@reviewer", in place of the CLI arguments. 




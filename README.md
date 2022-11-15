# ProVerB: Dataset of Tools and Formats for Program Verification

ProVerB is a project aimed at explaining program verification tools to help people find their way around the available tools, clearly and briefly summarising the main purpose of each tool, its current status, relations to other tools, etc.

Browse the data at [https://slebok.github.io/proverb/](https://slebok.github.io/proverb/)!

You can read more about how we set up this dataset in our MODELS '22 paper "[Modelling Program Verification Tools for Software Engineers](https://doi.org/10.1145/3550355.3552426)".

## Contributing
Do you want to add your own tool or fix some inaccuracy? *Feel free to create a PR!*
For tool pages we use a template which can be found [here](https://github.com/Sophietje/Verification-Tool-Overview/blob/main/Template%20tool%20page.md).

If you have an idea for a cool new feature you'd like to have or some interesting ideas to extend this project, please add an issue or send us an email :)

## Structure of the repo
Below you can find a description of what the different directories contain:
- **Conferences**: Links to all the papers that we have categorised.
- **Formats**: Each page describes a format/language that is used by verification tools.
- **Techniques**: Each page describes a technique/algorithm, not a specific tool.
- **Tools**: Each page describes a tool. We try to include a short description of what it does, if possible a link to the code/tool/repository, and information about tools used as back-ends.
- **Tools/Libraries**: Subdirectory of "Tools". All tools that are libraries/APIs are moved to this subdirectory.
- **Tools/Metatools**: Subdirectory of "Tools". All tools that are metatools are moved to this subdirectory.

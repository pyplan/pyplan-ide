ace.define("ace/snippets/ade",
  ["require", "exports", "module"],
  function (require, exports, module) {
    "use strict";

    exports.snippetText = "# IF\n\
    snippet if_struct\n\
      if ${1:check_expression} Then (\n\
        ${2:{Add for true here}}\n\
      )\n\
      else (\n\
        ${3:{Add for false here}}\n\
      )\n\
    # Create While\n\
    snippet while_struct\n\
      While  ${1:check_expression} Do \n\
      BEGIN \n\
        ${2:{Add body here}}\n\
      END\n\
      ";
    exports.scope = "ade";

  });

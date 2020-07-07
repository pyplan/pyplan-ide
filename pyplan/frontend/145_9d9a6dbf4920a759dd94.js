/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[145],{2656:function(e,a,n){"use strict";(function(t,i){var o,r,d=n(18);n(2657),o=[n(220),n(767),n(2659)],void 0===(r=function(e,a,o){return t.View.extend({$el:null,currentNodeId:"",diagram:void 0,dic:{},currentNode:null,fromWindowResize:!1,render:function(){var e=this,a=o({notDesktop:!1});i("#nodeWizardTab").append(a),this.$el=i(".nodeWizardTab"),e.createEditor(),e.dockedWindowWidth=i(".mainTask.influence-diagram .dockInfluenceDiagramProperty").width();e.maxCodeWidth=70*e.dockedWindowWidth/100,i(".codeArea").resizable({minWidth:200,maxWidth:e.maxCodeWidth,handles:"e",create:function(a,n){i("#nodeWizardEval").width(e.dockedWindowWidth-e.maxCodeWidth-12),e.$el.find(".resultArea").width(e.dockedWindowWidth-e.maxCodeWidth-12)},resize:function(a,n){i("#nodeWizardEval").width(e.dockedWindowWidth-e.$el.find(".codeArea").width()-12),e.$el.find(".resultArea").width(e.dockedWindowWidth-e.$el.find(".codeArea").width()-12)},stop:function(a,n){i("#nodeWizardEval").width(e.dockedWindowWidth-e.$el.find(".codeArea").width()-12),e.$el.find(".resultArea").width(e.dockedWindowWidth-e.$el.find(".codeArea").width()-12),i.cookie("resultAreaWidth",e.dockedWindowWidth-e.$el.find(".codeArea").width()-12,{expires:365})}}),(0,d.isIE)()&&(i(".mainTask.influence-diagram").off("diagramClick"),i(".mainTask.influence-diagram").on("diagramClick",(function(a){var n=ace.edit("nodeWizardDef");if(n&&e.nodeData&&e.currentValue){var t=n.getValue();if(e.currentValue!==t&&null!==t&&t){var o=i(".nodeWizardDef").attr("data-rel");e.updateNodePropertyNew(e.nodeData,o,t)}}}))),i.isEmptyObject(e.options.dic)?i(".moreChangesContainer").hide():i(".moreChangesContainer").show(),i(".dropdownPending").perfectScrollbar(),this.$el.on("updateNodeId",(function(a,n){e.nodeFullData.id=n})),this.$el.on("clickNode",(function(a,n){var t=n.nodeFullData,o=n.nodeProperties,r=n.forcePreview,d=n.isDecision;e.$el.find(".save, .cancel").attr("disabled",!0),e.nodeFullData=t,e.currentNode=o;var l="true"===e.getNodeProperty(o.properties,"isCalc").value.toLowerCase();!0===d&&delete e.options.dic[e.currentNode.node];var s=function(){return e.previewNode(r)};e.options.dic[e.currentNode.node]?(e.currentNode.properties.forEach((function(a){var n=e.options.dic[e.currentNode.node].properties.find((function(e){return e.name===a.name}));n&&(a.value=n.value)})),e.populateData(e.currentNode,s),i(".btnsConfirmChanges").show(),i('.btn[data-action="run"]').addClass("btn-warning").removeClass("btn-info"),i(".resultPreview").css("color","#999"),i(".moreChangesContainer").show(),i(".btnDataFrame").hide(),i(".btnDataArray").hide(),i(".btnInputTable").hide(),i("body").trigger("pendingChanges",[!0])):(e.populateData(e.currentNode,s),i(".btnsConfirmChanges").hide(),i.isEmptyObject(e.options.dic)&&i(".moreChangesContainer").hide()),l?(i('.btn[data-action="run"]').addClass("btn-info").removeClass("btn-warning"),i(".resultPreview").css("color","inherit")):(i('.btn[data-action="run"]').addClass("btn-warning").removeClass("btn-info"),i(".resultPreview").css("color","#999"))})),this.$el.on("deleteSelectedNodes",(function(a,n){i.each(n,(function(a,n){delete e.options.dic[n]})),i.isEmptyObject(e.options.dic)&&i(".moreChangesContainer").hide()})),i(".mainTask.influence-diagram").on("addNodeToWizardDefinition",(function(a,n){if(i(".nodeWizardTab").is(":visible")){var t=ace.edit("nodeWizardDef");t&&(t.insert(n),e.updateNodePropertyNew(e.nodeData,"definition",t.getValue()))}})),this.$el.on("updateSizes",(function(a,n){e.fromWindowResize=!1,e.updateSizes()})),i(window).on("resize",(function(){event.target==window&&"resize"==event.type&&(e.fromWindowResize=!0,e.updateSizes(event,{tipo:"windowResize"}))})),this.updateSizes(),this.addHandlers()},previewNode:function(a){var n=this,t=i("#nodeWizardEval"),o=this.nodeData.node,r=t.find(".btnDataFrame"),d=t.find(".btnDataArray"),l=t.find(".btnInputTable"),s=t.find(".btnStopProcess"),c=t.find(".btnIndex"),u=t.find(".btnCopyAsValues"),p=t.find(".atomic"),m=p.find("pre");(r.hide(),d.hide(),l.hide(),u.hide(),c.hide(),p.hide(),m.empty(),a||"true"===this.getNodeProperty(this.nodeData.properties,"isCalc").value.toLowerCase())?(i('button[data-action="debug"]').attr("disabled",!0),s.show(),(new e).previewNode(o,(function(e){if(i('button[data-action="run"]').removeClass("btn-warning").addClass("btn-info"),i('button[data-action="debug"]').attr("disabled",!1),i(".resultPreview").css("color","inherit"),s.hide(),t.find(".evaluating").hide(),e){p.show();var a="";if(a=e.console?e.console+e.preview:e.preview,m.text(a),e.resultType){r.toggle(!n.options.dic[n.currentNode.node]&&["<class 'pandas.core.frame.dataframe'>"].includes(e.resultType.toLowerCase()));var o=!n.options.dic[n.currentNode.node]&&["<class 'xarray.core.dataarray.dataarray'>"].includes(e.resultType.toLowerCase());if(d.toggle(o&&n.nodeFullData&&"inputtable"!==n.nodeFullData.nodeClass),l.toggle(o&&n.nodeFullData&&"inputtable"==n.nodeFullData.nodeClass),["<class 'pandas.core.indexes.base.index'>"].includes(e.resultType.toLowerCase())){var f=n.getNodeProperty(n.nodeData.properties,"definition").value.replace(/ /g,"").replace(/'/g,'"');c.toggle(f.startsWith('result=pd.Index(["'))}u.toggle(["<class 'xarray.core.dataarray.dataarray'>","<class 'pandas.core.indexes.base.index'>"].includes(e.resultType.toLowerCase())&&n.nodeFullData&&"inputtable"!=n.nodeFullData.nodeClass)}}}),(function(e){t.find(".evaluating").hide(),t.find(".error div").text(e),t.find(".error").show(),s.hide(),i('button[data-action="debug"]').attr("disabled",!1)}))):(s.hide(),r.hide(),d.hide(),l.hide(),c.hide(),u.hide())},updateSizes:function(e){if(this.$el){var a=this;if(0==i("#nodeWizardDef").length)return;var n=ace.edit("nodeWizardDef"),t=i(".mainTask.influence-diagram .dockInfluenceDiagramProperty").height();a.dockedWindowWidth=i(".mainTask.influence-diagram .dockInfluenceDiagramProperty").width();var o=i(".leftCol").width(),r=t-70;i(n.container).height(r),i(n.container).find(".ace_content").height(r),i(n.container).find(".ace_content").width(a.dockedWindowWidth-(o+50)),n.resize();var d=0;a.maxCodeWidth=70*a.dockedWindowWidth/100,d=a.maxCodeWidth,i(".codeArea").resizable("option","maxWidth",a.maxCodeWidth);var l=i.cookie("resultAreaWidth")?a.dockedWindowWidth-parseInt(i.cookie("resultAreaWidth")):d;i.cookie("resultAreaWidth")&&parseInt(i.cookie("resultAreaWidth"))<=a.maxCodeWidth&&(d=l),0===a.$el.find(".codeArea").width()?a.$el.find(".codeArea").width(d):(i(".dockInfluenceDiagramProperty").trigger("updateWidth"),1==a.fromWindowResize&&(setTimeout((function(){i(".codeArea").resizable("option","maxWidth",a.maxCodeWidth),a.$el.find(".codeArea").width(d),a.dockedWindowWidth=i(".mainTask.influence-diagram .dockInfluenceDiagramProperty").width(),a.maxCodeWidth=70*a.dockedWindowWidth/100,i("#nodeWizardEval").width(a.dockedWindowWidth-d-12),a.$el.find(".resultArea").width(a.dockedWindowWidth-d-12),i(".dockInfluenceDiagramProperty").trigger("updateWidth")}),800),a.fromWindowResize=!1)),this.$el.find(".resultArea").height(r),this.$el.find(".resultPreview").height(r-20)}},populateData:function(e){var a=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null,n=this,t=ace.edit("nodeWizardDef");if(t&&t.blur(),setTimeout((function(){n.loadData(e),"function"==typeof a&&a()}),500),e.disabledFields)for(var i=0;i<e.disabledFields.length;i++)this.$el.find("#"+e.disabledFields[i]).prop("disabled",!0),t&&"nodeWizardDef"==e.disabledFields[i]&&n.disableEditor(t)},loadData:function(e){this.nodeData=e,i("#nodeTypeIcon").removeClass((function(e,a){return(a.match(/(^|\s)nodeClassIcon-\S+/g)||[]).join(" ")})),i("#nodeTypeIcon").addClass("nodeClassIcon-"+e.properties[2].value.toLowerCase());var a=e.properties[4].value,n=ace.edit("nodeWizardDef");n.setValue(""),n.getSession().setUseWrapMode(!0);var t=e.properties[2].value.toUpperCase();["MODULE","LIBRARY","LINKMODULE","MODEL","TEXT","PICTURE"].includes(t)?this.disableEditor(n):(this.onBrowserMode()||"INPUTTABLE"==t?this.disableEditor(n):this.enableEditor(n),null===a&&(a=""),n.setValue(a,1),this.currentValue=a,n.session.setValue(a),n.renderer.updateFull()),""!==e.properties[6].value?this.loadErrorTab(e.properties[5].value):this.cleanErrorTab(),this.updateSizes()},disableEditor:function(e){e.setReadOnly(!0),i(e.container).addClass("aceDisabled")},enableEditor:function(e){e.setReadOnly(!1),i(e.container).removeClass("aceDisabled")},createEditor:function(){var a=this,n=i(".nodeWizardDef").get()[0],t=ace.require("ace/ext/language_tools"),o=ace.edit(n);o.on("change",(function(e){var n=o.getValue(),t=i(".nodeWizardDef").attr("data-rel");o.curOp&&o.curOp.command.name?a.updateNodePropertyNew(a.nodeData,t,n):i(".ace_replacebtn").is(":visible")&&(a.updateNodePropertyNew(a.nodeData,t,n),o.focus())})),o.setTheme("ace/theme/cubeplan"),o.session.setMode("ace/mode/python"),o.$blockScrolling=1/0,o.setHighlightActiveLine(!1),o.commands.addCommand({name:"saveDefinition",bindKey:{win:"Ctrl-s",mac:"Command-s"},exec:function(e){setTimeout((function(){e.focus(),i(".btnSaveModel").is(":visible")&&i(".btnSaveModel").trigger("click")}),100)}}),o.commands.addCommand({name:"saveDefinitionEnter",bindKey:{win:"Ctrl-Enter",mac:"Command-Enter"},exec:function(e){setTimeout((function(){e.focus(),a.options.dic[a.currentNode.node]?a.saveModel((function(){a.previewNode(!0)})):a.previewNode(!0)}),100)}}),o.commands.addCommand({name:"onlySaveDefinitionEnter",bindKey:{win:"Shift-Enter",mac:"Shift-Enter"},exec:function(e){setTimeout((function(){e.focus(),a.options.dic[a.currentNode.node]&&a.saveModel((function(){}))}),100)}}),o.commands.addCommand({name:"toggleShowIdentifier",bindKey:{win:"Ctrl-y",mac:"Command-y"},exec:function(e){i(".mainTask.influence-diagram").trigger("onKeyDown",["ctrl+y"])}}),o.commands.addCommand({name:"gotoDef",bindKey:{win:"Ctrl-h",mac:"Command-h"},exec:function(e){if(e.getValue()){var n=e.getSelection(),t=e.getSession();if(n){var i=n.getWordRange();try{var o=t.getTextRange(i);o&&a.$el.closest(".influence-diagram").find(".diagram-area").trigger("navigateToNode",[o])}catch(e){}}}}});var r=o.completers?o.completers.slice(0):[],d={getCompletions:function(a,n,t,i,o){for(var d=[],l=0;l<r.length;l++)r[l].getCompletions(a,n,t,i,(function(e,a){a&&(d=d.concat(a))}));(new e).SearchForAutocomplete(i,(function(e){var a=n.$mode.$highlightRules.completions;a||(a=[]);var t=a.concat(d);e&&((t=t.concat(e.map((function(e){return{caption:e.id,value:e.completeText,meta:e.nodeClass,docHTML:"function"==e.nodeClass||"class"==e.nodeClass||"helper"==e.nodeClass||"method"==e.nodeClass?"<b>"+(e.params?e.params:e.name)+"</b><hr>"+(e.description?e.description:""):"<b>"+e.name+"</b>",params:e.params}})))).forEach((function(e){if(!e.snippet){var a=null;if("function"!=e.meta&&"class"!=e.meta&&"SysFunction"!=e.meta&&"helper"!=e.meta&&"method"!=e.meta||!e.params)"index value"!=e.meta&&"cube axis"!=e.meta&&"dataframe column"!=e.meta||!e.params||(a=e.value+e.params,e.snippet=a);else{a=e.value+"( ";for(var n=1,t=e.params.split(";"),i=0;i<t.length;i++){var o=t[i];if(o)for(var r=o.split(","),d=0;d<r.length;d++){var l=r[d];if(l&&-1==l.toLowerCase().indexOf("hidden")){n>1&&(a+=", ");var s=l.replace("(","").replace(")","").trim();s.indexOf(":")>=0&&(s=s.split(":")[0]),a+="${"+n+":"+s+"}",n++}}}a+=" )",e.snippet=a}}})),o(null,t))}))},getDocTooltip:function(e){"snippet"!=e.type||e.docHTML||(e.docHTML=["<b>",e.caption,"</b>","<hr></hr>",e.snippet].join(""))}};t.addCompleter(d),o.setOptions({enableBasicAutocompletion:!0,enableSnippets:!0,enableLiveAutocompletion:!1,showPrintMargin:!1})},addHandlers:function(){var a=this,t=this;this.$el.find(".commandBtns .btn").on("click",(function(o){switch(i(o.currentTarget).attr("data-action")){case"run":i(o.currentTarget).removeClass("btn-warning").addClass("btn-info"),t.currentNode&&(t.options.dic[t.currentNode.node]?a.saveModel((function(){a.previewNode(!0)})):a.previewNode(!0));break;case"debug":n.e(6).then((function(){var e=[n(682)];(function(e){var n=new e,t=a.nodeData.node,i=a.nodeData.properties.find((function(e){return"title"===e.name})).value||"";n.debugNode({nodeId:t,nodeTitle:i})}).apply(null,e)})).catch(n.oe);break;case"stop":i(o.currentTarget).hide(),(new e).stopProcess();break;case"wiz-columns":Promise.resolve().then((function(){var e=[n(698)];(function(e){(new e).selectColumsWizard({title:(0,d.translate)("_select_columns"),bodyParams:{wizard:"SelectColumns",action:"getColumnList",params:{nodeId:t.currentNode.node}},confirm:{wizard:"SelectColumns",action:"generateDefinition",params:{nodeId:t.currentNode.node,columns:[]}}},(function(){}))}).apply(null,e)})).catch(n.oe);break;case"wiz-rows":Promise.resolve().then((function(){var e=[n(698)];(function(e){(new e).selectRowsWizard({title:(0,d.translate)("filter"),bodyParams:{wizard:"SelectRows",action:"getColumnList",params:{nodeId:t.currentNode.node,includeColumnList:!0}},confirm:{wizard:"SelectRows",action:"generateDefinition",params:{nodeId:t.currentNode.node,filters:[]}}},(function(){Promise.resolve().then((function(){var e=[n(746)];(function(e){(new e).loadDefinitionTab(t.nodeFullData,!1,".btnTabWizard",!0)}).apply(null,e)})).catch(n.oe)}))}).apply(null,e)})).catch(n.oe);break;case"wiz-calc":Promise.resolve().then((function(){var e=[n(698)];(function(e){(new e).calculatedFieldWizard({title:(0,d.translate)("_calculated_field"),bodyParams:{wizard:"CalculatedField",action:"getColumnList",params:{nodeId:t.currentNode.node}},confirm:{wizard:"CalculatedField",action:"generateDefinition",params:{nodeId:t.currentNode.node}}},(function(){Promise.resolve().then((function(){var e=[n(746)];(function(e){(new e).loadDefinitionTab(t.nodeFullData,!1,".btnTabWizard",!0)}).apply(null,e)})).catch(n.oe)}))}).apply(null,e)})).catch(n.oe);break;case"wiz-edit-index":Promise.resolve().then((function(){var e=[n(698)];(function(e){(new e).editIndexWizard({title:(0,d.translate)("_edit_index"),onBrowserMode:t.onBrowserMode(),bodyParams:{wizard:"EditIndex",action:"getIndexItems",params:{nodeId:t.currentNode.node}},confirm:{wizard:"EditIndex",action:"generateDefinition",params:{nodeId:t.currentNode.node,values:[]}}},(function(e){i("#nodePropertiesDock").trigger("refreshNodeDefinition",[e,!0])}))}).apply(null,e)})).catch(n.oe);break;case"wiz-rename-index-item":Promise.resolve().then((function(){var e=[n(698)];(function(e){(new e).renameIndexItemWizard({title:(0,d.translate)("_rename_index_item"),onBrowserMode:t.onBrowserMode(),bodyParams:{wizard:"RenameIndexItem",action:"getIndexItems",params:{nodeId:t.currentNode.node}},confirm:{wizard:"RenameIndexItem",action:"generateDefinition",params:{nodeId:t.currentNode.node,values:[]}}},(function(e){i("#nodePropertiesDock").trigger("refreshNodeDefinition",[e,!0])}))}).apply(null,e)})).catch(n.oe);break;case"wiz-copyasvalues":(new e).copyAsValues(t.currentNode.node,!o.ctrlKey,(function(e){t.$el.closest(".influence-diagram").trigger("refreshView"),o.ctrlKey&&Promise.resolve().then((function(){var e=[n(746)];(function(e){(new e).loadDefinitionTab(t.nodeFullData,!1,".btnTabWizard",!0)}).apply(null,e)})).catch(n.oe)}));break;case"wiz-dataframe-index":Promise.resolve().then((function(){var e=[n(698)];(function(e){(new e).setDataframeIndex({title:(0,d.translate)("_set_index"),bodyParams:{wizard:"DataframeIndex",action:"getColumnList",params:{nodeId:t.currentNode.node}},confirm:{wizard:"DataframeIndex",action:"generateDefinition",params:{nodeId:t.currentNode.node,columns:[]}}},(function(){Promise.resolve().then((function(){var e=[n(746)];(function(e){(new e).loadDefinitionTab(t.nodeFullData,!1,".btnTabWizard",!0)}).apply(null,e)})).catch(n.oe)}))}).apply(null,e)})).catch(n.oe);break;case"wiz-dataframe-index-from-pandas":Promise.resolve().then((function(){var e=[n(698)];(function(e){(new e).indexFromPandas({title:(0,d.translate)("_create_index"),bodyParams:{wizard:"DataframeIndex",action:"getColumnList",params:{nodeId:t.currentNode.node}},confirm:{wizard:"IndexFromPandas",action:"generateDefinition",params:{nodeId:t.currentNode.node,indexes:[]}}},(function(e){i(".mainTask.influence-diagram .diagram-area").trigger("navigateToNode",[e,!0])}))}).apply(null,e)})).catch(n.oe);break;case"wiz-dataframe-groupby":Promise.resolve().then((function(){var e=[n(698)];(function(e){(new e).dataframeGroupby({title:"".concat((0,d.translate)("_group"),"/").concat((0,d.translate)("aggregate")),bodyParams:{wizard:"DataframeGroupby",action:"getColumnList",params:{nodeId:t.currentNode.node}},confirm:{wizard:"DataframeGroupby",action:"generateDefinition",params:{nodeId:t.currentNode.node,columns:[],agg:{}}}},(function(){Promise.resolve().then((function(){var e=[n(746)];(function(e){(new e).loadDefinitionTab(t.nodeFullData,!1,".btnTabWizard",!0)}).apply(null,e)})).catch(n.oe)}))}).apply(null,e)})).catch(n.oe);break;case"wiz-dataarray-from-pandas":Promise.resolve().then((function(){var e=[n(698)];(function(e){(new e).dataarrayFromPandas({title:(0,d.translate)("create_dataarray"),bodyParams:{wizard:"DataarrayFromPandas",action:"getDataframeSchema",params:{nodeId:t.currentNode.node}},confirm:{wizard:"DataarrayFromPandas",action:"generateDefinition",params:{nodeId:t.currentNode.node,indexes:[],agg:{}}}},(function(e){i(".mainTask.influence-diagram .diagram-area").trigger("navigateToNode",[e,!0])}))}).apply(null,e)})).catch(n.oe);break;case"wiz-inputtable":Promise.resolve().then((function(){var e=[n(698)];(function(e){(new e).inputTable({nodeId:t.currentNode.node})}).apply(null,e)})).catch(n.oe);break;default:break;case"wiz-dataarray-filter":Promise.resolve().then((function(){var e=[n(698)];(function(e){(new e).dataArrayFilter({title:(0,d.translate)("filter"),bodyParams:{wizard:"DataArrayFilter",action:"getDataArrayDimensions",params:{nodeId:t.currentNode.node}},confirm:{wizard:"DataArrayFilter",action:"generateDefinition",params:{nodeId:t.currentNode.node,filters:{}}}},(function(){Promise.resolve().then((function(){var e=[n(746)];(function(e){(new e).loadDefinitionTab(t.nodeFullData,!1,".btnTabWizard",!0)}).apply(null,e)})).catch(n.oe)}))}).apply(null,e)})).catch(n.oe)}})),i(".dockInfluenceDiagramProperty").find(".btnCancel").on("click",(function(e){delete t.options.dic[t.currentNode.node],Promise.resolve().then((function(){var e=[n(746)];(function(e){(new e).loadDefinitionTab(t.nodeFullData)}).apply(null,e)})).catch(n.oe)})),i(".dockInfluenceDiagramProperty .btnSave").on("click",(function(){return a.saveModel()})),i(".dockInfluenceDiagramProperty").on("saveCurrentNode",(function(){var a=new e,n=[];t.currentNode&&t.options.dic[t.currentNode.node]&&(i.each(t.options.dic[t.currentNode.node].properties,(function(e,a){["defErrorDetail","errorInDef","class","isCalc","resultType"].includes(a.name)||n.push(a)})),a.setNodeProperties(t.currentNode.node,n,(function(e){delete t.options.dic[t.currentNode.node],i(".btnsConfirmChanges").hide(),i.isEmptyObject(t.options.dic)&&i(".moreChangesContainer").hide(),i(".mainTask.influence-diagram").trigger("refreshView"),t.cleanErrorTab()}),(function(e){t.loadErrorTab(e),delete t.options.dic[t.currentNode.node],i(".mainTask.influence-diagram").trigger("refreshView"),i(".overlapDisable").hide(),i(".btnsConfirmChanges").hide(),i.isEmptyObject(t.options.dic)&&i(".moreChangesContainer").hide()}),!0,!0))})),i(".dockInfluenceDiagramProperty").on("saveModelChanges",(function(a,o,r){var l,s,c=new e,u=[];if(i.isEmptyObject(t.options.dic)&&!o)Promise.resolve().then((function(){var e=[n(220)];(function(e){(new e).saveModel((function(){i("body").trigger("pendingChanges",[!1]),(0,d.showMessage)((0,d.translate)("model_successfully_saved"),(0,d.translate)("_successfully_saved"),"success",!0),r&&r(!0)}))}).apply(null,e)})).catch(n.oe);else if(i.isEmptyObject(t.options.dic)&&o&&r)r(!0);else for(var p in t.options.dic)u=[],i.each(t.options.dic[p].properties,(function(e,a){["defErrorDetail","errorInDef","class","isCalc","resultType","Text"].includes(a.name)||u.push(a)})),l=t.nodeFullData.id,s=t.nodeFullData.nodeClass,c.setNodeProperties(t.options.dic[p].node,u,(function(e){delete t.options.dic[p],i(".btnsConfirmChanges").hide(),"text"===s&&(i(".box-title.header .nodeIdTitle").remove(),i(".dock.dockItem .nodeTextTitle").html("(".concat(l,")"))),i.isEmptyObject(t.options.dic)&&i(".moreChangesContainer").hide(),i(".mainTask.influence-diagram").trigger("refreshView"),t.cleanErrorTab(),i.isEmptyObject(t.options.dic)&&!o&&Promise.resolve().then((function(){var e=[n(220)];(function(e){(new e).saveModel((function(){i("body").trigger("pendingChanges",[!1]),(0,d.showMessage)((0,d.translate)("model_successfully_saved"),(0,d.translate)("_successfully_saved"),"success",!0),r&&r(!0)}))}).apply(null,e)})).catch(n.oe)}),(function(e){t.loadErrorTab(e),delete t.options.dic[t.currentNode.node],i(".mainTask.influence-diagram").trigger("refreshView"),i(".overlapDisable").hide(),i(".btnsConfirmChanges").hide(),i.isEmptyObject(t.options.dic)&&i(".moreChangesContainer").hide(),r&&r(!1)}),!0,!1)}))},saveModel:function(a){var n=new e,t=[],o=this;i.each(this.options.dic[o.currentNode.node].properties,(function(e,a){["defErrorDetail","errorInDef","class","isCalc","resultType"].includes(a.name)||t.push(a)}));var r=o.currentNode.properties[0].value,d=o.currentNode.properties[2].value;n.setNodeProperties(o.currentNode.node,t,(function(e){i(".mainTask.influence-diagram").trigger("refreshView"),i(".dashboard-tabs").trigger("refreshNodeChanges",[{nodeId:o.currentNode.node}]),"text"===d&&(i(".box-title.header .nodeIdTitle").remove(),i(".dock.dockItem .nodeTextTitle").html("(".concat(r,")"))),delete o.options.dic[o.currentNode.node],i(".btnsConfirmChanges").hide(),i.isEmptyObject(o.options.dic)&&i(".moreChangesContainer").hide(),o.cleanErrorTab(),"function"==typeof a&&a()}),(function(e){o.loadErrorTab(e),delete o.options.dic[o.currentNode.node],i(".mainTask.influence-diagram").trigger("refreshView"),i(".overlapDisable").hide(),i(".btnsConfirmChanges").hide(),i.isEmptyObject(o.options.dic)&&i(".moreChangesContainer").hide()}),!0,!0)},setNumberFormat:function(e){if((t=this).nodeData.properties[0].value){var a=t.nodeData.properties[0].value,t=this;Promise.resolve().then((function(){var o=[n(220)];(function(n){var o=[{name:"numberFormat",value:e}](new n).setNodeProperties(a,o,(function(){t.numberFormat=e,t.numberFormatter=null,i(".dashboardTask").trigger("changeNumberFormat",[a]),i(".mainTask.influence-diagram").trigger("refreshView")}))}).apply(null,o)})).catch(n.oe)}},showNumberFormatPopup:function(e){var a=this;Promise.resolve().then((function(){var t=[n(220)];(function(t){var i=[{name:"numberFormat"}](new t).getNodeProperties(a.nodeData.properties[0].value,i,(function(a){var t=a.properties[0];n.e(48).then((function(){var a=[n(803)];(function(a){(new a).render(t,e)}).apply(null,a)})).catch(n.oe)}))}).apply(null,t)})).catch(n.oe)},updateNodeInDic:function(e,a){this.nodeData&&this.nodeData.properties&&this.nodeData.properties[0]&&this.nodeData.properties[0].value&&this.options.dic[e]&&(this.options.dic[a]=this.options.dic[e],delete this.options.dic[e],this.currentNodeId=a,this.nodeData.node=a,this.nodeData.properties[0].value=a,i("#nodePropertiesDock").attr("node-id",a))},getNodeProperty:function(e,a){return e.find((function(e){return e.name===a}))},updateNodePropertyNew:function(e,a,n){var t=this;i.each(e.properties,(function(o,r){r.name===a&&(r.value!==n&&(t.options.dic[e.node]||(t.options.dic[e.node]={node:e.node,properties:[]},i(".btnsConfirmChanges").show(),i(".moreChangesContainer").show(),i('.btn[data-action="run"]').addClass("btn-warning").removeClass("btn-info"),i(".resultPreview").css("color","#999"),i(".btnDataFrame").hide(),i(".btnDataArray").hide(),i(".btnInputTable").hide(),i(".btnCopyAsValues").hide(),i(".btnCopyAsValues").hide(),i(".btnIndex").hide(),i("body").trigger("pendingChanges",[!0])),t.options.dic[e.node].properties.some((function(e){return e.name===a}))?t.options.dic[e.node].properties.find((function(e){return e.name===a})).value=n:t.options.dic[e.node].properties.push({name:a,value:n})))}))},updateNodeProperty:function(a,n,t){var o=arguments.length>3&&void 0!==arguments[3]?arguments[3]:null,r=this,d=a.properties[0].value;if(""!==d){var l=new e;l.setNodeProperties(d,[{name:n,value:t}],(function(){if(i(".mainTask.influence-diagram").trigger("refreshView"),r.cleanErrorTab(),"definition"===n){var e=ace.edit("nodeWizardDef");e.setValue(t);var d=e.selection.getCursor();e.focus(),e.gotoLine(d.row,d.column,!0),e.moveCursorTo(d.row,d.column)}a.properties.find((function(e){return e.name===n})).value=t,"function"==typeof o&&o()}),(function(e){r.loadErrorTab(e),i(".mainTask.influence-diagram").trigger("refreshView")}),!0,!0)}},onBrowserMode:function(){return 0==i(".mainTask.influence-diagram .diagram-area .diagram-toolbar").length||i(".mainTask.influence-diagram .diagram-area .diagram-toolbar").hasClass("browser-mode")},loadErrorTab:function(e){var a=i(".errorsList");a.find("i.no-error").addClass("error"),a.find(".errorCount").html("1"),a.find(".message-ul .details .message").html(e),a.find("a").attr("data-toggle","dropdown")},cleanErrorTab:function(){var e=i(".errorsList");e.find("i.no-error").removeClass("error"),e.find(".errorCount").html("0"),e.find(".message-ul .details .message").html(""),e.find("a").attr("data-toggle","")},onRemoveView:function(){(0,d.removeResizeEvent)("updateSizes"),this.diagram&&(this.diagram.destroy(),this.diagram=null)}})}.apply(a,o))||(e.exports=r)}).call(this,n(219),n(1))},2657:function(e,a,n){var t=n(2658);"string"==typeof t&&(t=[[e.i,t,""]]);var i={hmr:!0,transform:void 0,insertInto:void 0};n(224)(t,i);t.locals&&(e.exports=t.locals)},2658:function(e,a,n){(e.exports=n(2)(!1)).push([e.i,".nodeWizardTab .commandBtns{width:100%;padding-left:0px;margin:-31px 0 2px 4px}.nodeWizardTab .commandBtns button{margin-right:0px;border-radius:0px;width:30px}.nodeWizardTab .resultArea{margin-top:7px;margin-right:0;margin-left:0}.nodeWizardTab .resultPreview{margin:0 0 0 6px}#wizardColSelection .modal-body{overflow-y:auto}#wizardColSelection .modal-body .optList ul{list-style:none}#wizardColSelection .modal-body .optList ul li{margin:1px 0}#wizardColSelection .commandButtons{padding:5px;border-top:1px solid #e5e5e5}#wizardColSelection .fa-success{color:#4caf50}#wizardColSelection .fa-danger{color:#f44336}#wizardRowSelection .modal-dialog{width:80%;max-width:800px}#wizardRowSelection .modal-body{overflow-y:auto}#wizardRowSelection .table .select2-container{width:100%}#wizardRowSelection .table .conditionValue input{width:100%}#wizardRowSelection .table .conditionValue.double input{width:45%}#wizardRowSelection .table .conditionValue.double input:nth-child(2){float:right}#wizardDataArrayFilter .modal-dialog{width:80%;max-width:800px}#wizardDataArrayFilter .modal-body{overflow-y:auto}#wizardDataArrayFilter .table .select2-container{width:100%}#wizardDataArrayFilter .table .conditionValue input{width:100%}#wizardDataArrayFilter .table .conditionValue input:nth-child(2){float:right}#wizardDataArrayFilter .commandButtons{padding:5px;border-top:1px solid #e5e5e5}#wizardEditIndex .modal-body{overflow-y:auto;min-height:300px;text-align:center;padding:10px}#wizardEditIndex .modal-body .handsonWrapper{display:inline-block}#wizardEditIndex .tableDef .ht_master .wtHolder{overflow-x:hidden}#wizardIndex .modal-body{overflow-y:auto;min-height:300px;text-align:center;padding:10px}#wizardIndex .modal-body .handsonWrapper{display:inline-block;text-align:center}#wizardIndex .modal-body .form-tooltip{height:32px;padding-top:8px}#wizardIndex .tableDef .ht_master .wtHolder{overflow-x:hidden}#wizardRenameIndexItem .modal-body{overflow-y:auto;min-height:300px;text-align:center;padding:10px}#wizardRenameIndexItem .modal-body .handsonWrapper{display:inline-block;text-align:center}#wizardRenameIndexItem .modal-body .form-tooltip{height:32px;padding-top:8px}#wizardRenameIndexItem .tableDef .ht_master .wtHolder{overflow-x:hidden}#wizardSetDataframeIndex .modal-body{overflow-y:auto}#wizardSetDataframeIndex .modal-body .optList ul{list-style:none}#wizardSetDataframeIndex .modal-body .optList ul li{margin:1px 0}#wizardSetDataframeIndex .commandButtons{padding:5px;border-top:1px solid #e5e5e5}#wizardDataframeGroupby .modal-dialog{width:80%;max-width:800px}#wizardDataframeGroupby .modal-dialog .modal-body{overflow-y:auto}#wizardDataframeGroupby .modal-dialog .modal-body .centered{text-align:center}#wizardDataframeGroupby .modal-dialog .modal-body .selectable{width:60px}#wizardDataframeGroupby .modal-dialog .modal-body .group-by{width:130px}#wizardDataframeGroupby .modal-dialog .modal-body .optList ul{list-style:none}#wizardDataframeGroupby .modal-dialog .modal-body .optList ul li{margin:1px 0}#wizardCalculatedField .modal-dialog{max-width:800px}#wizardDataarrayFromPandas .modal-dialog{width:85%;max-width:1000px}#wizardDataarrayFromPandas .modal-dialog .modal-body{overflow-y:auto}#wizardDataarrayFromPandas .modal-dialog .modal-body .centered{text-align:center}#wizardDataarrayFromPandas .modal-dialog .modal-body .selectable{width:60px}#wizardDataarrayFromPandas .modal-dialog .modal-body .group-by{width:130px}#wizardDataarrayFromPandas .modal-dialog .modal-body .optList ul{list-style:none}#wizardDataarrayFromPandas .modal-dialog .modal-body .optList ul li{margin:1px 0}#wizardDataarrayFromPandas .modal-dialog .modal-body .optList tr td.wizard-field i{display:none}#wizardDataarrayFromPandas .modal-dialog .modal-body .optList tr.selected td.wizard-field i{display:inline}#wizardDataarrayFromPandas .modal-dialog .modal-body .optList tr.selected td.wizard-field span{color:#378ee0}#wizardIndexFromPandas .modal-body{overflow-y:auto}#wizardInputTable .modal-dialog{width:85%;max-width:1000px}.indexlist li{padding:0;cursor:pointer;border-bottom:1px solid #ccc;display:block}.indexlist li:hover{background:#e7f1fb;color:#333}.indexlist li.j-focused{background:#e7f1fb}.indexlist li.j-selected{background:#dcebf9}.indexlist li .node{padding:1px 2px 2px 0px;display:block}.indexlist li span.nodeTitle{display:block;margin-left:5px}.indexlist li span.nodeId{display:block;margin-left:5px;font-style:italic;font-size:.9em}",""])},2659:function(e,a,n){var t=n(670);function i(e){return e&&(e.__esModule?e.default:e)}e.exports=(t.default||t).template({1:function(e,a,t,o,r){return"      <button class='btn btn-small btn-lightred btnStopProcess nodisplay' rel='tooltip'\n        data-original-title='"+e.escapeExpression(i(n(668)).call(null!=a?a:e.nullContext||{},"stop",{name:"L",hash:{},data:r,loc:{start:{line:18,column:29},end:{line:18,column:41}}}))+"' data-action='stop'>\n        <i class='fa fa-stop'></i>\n      </button>\n"},compiler:[8,">= 4.3.0"],main:function(e,a,t,o,r){var d,l=null!=a?a:e.nullContext||{},s=e.escapeExpression,c=e.lookupProperty||function(e,a){if(Object.prototype.hasOwnProperty.call(e,a))return e[a]};return"<div class='row nodeWizardTab nomargin'>\n  <div class='nopadding codeArea' style=\"float: left;\">\n    <div class='aceWrapper'>\n      <div id='nodeWizardDef' class='nodeWizardDef' data-rel='definition' style='width:100%; height:170px;'></div>\n    </div>\n  </div>\n  <div id='nodeWizardEval' class='leftCol nopadding' style=\"right:0; float: left;\">\n    <div class='commandBtns'>\n      <button class='btn btn-small btn-warning' rel='tooltip' data-original-title='"+s(i(n(668)).call(l,"_run",{name:"L",hash:{},data:r,loc:{start:{line:9,column:83},end:{line:9,column:95}}}))+"' data-action='run'>\n        <i class='fa fa-play'></i>\n      </button>\n      <button class='btn btn-small btn-lightgrey' rel='tooltip' data-original-title='"+s(i(n(668)).call(l,"debug_node",{name:"L",hash:{},data:r,loc:{start:{line:12,column:85},end:{line:12,column:103}}}))+"'\n        data-action='debug'>\n        <i class='fa fa-stopwatch'></i>\n      </button>\n"+(null!=(d=c(t,"if").call(l,null!=a?c(a,"notDesktop"):a,{name:"if",hash:{},fn:e.program(1,r,0),inverse:e.noop,data:r,loc:{start:{line:16,column:6},end:{line:21,column:13}}}))?d:"")+"      <button class='btn btn-small btn-lightgrey btnDataFrame nodisplay' rel='tooltip'\n        data-original-title='"+s(i(n(668)).call(l,"_select_columns",{name:"L",hash:{},data:r,loc:{start:{line:23,column:29},end:{line:23,column:52}}}))+"' data-action='wiz-columns'>\n        <i class=\"fad fa-line-columns\"></i>\n      </button>\n      <button class='btn btn-small btn-lightgrey btnDataFrame nodisplay' rel='tooltip'\n        data-original-title='"+s(i(n(668)).call(l,"filter",{name:"L",hash:{},data:r,loc:{start:{line:27,column:29},end:{line:27,column:43}}}))+"' data-action='wiz-rows'>\n        <i class='far fa-filter'></i>\n      </button>\n      <button class='btn btn-small btn-lightgrey btnDataFrame nodisplay' rel='tooltip'\n        data-original-title='"+s(i(n(668)).call(l,"_calculated_field",{name:"L",hash:{},data:r,loc:{start:{line:31,column:29},end:{line:31,column:54}}}))+'\' data-action=\'wiz-calc\'>\n        <i class="fal fa-calculator-alt"></i>\n      </button>\n      <button class="btn btn-small btn-lightgrey btnDataFrame nodisplay" rel="tooltip"\n        data-original-title=\''+s(i(n(668)).call(l,"_set_index",{name:"L",hash:{},data:r,loc:{start:{line:35,column:29},end:{line:35,column:47}}}))+'\' data-action="wiz-dataframe-index" style="height:26px; padding:0">\n        <span class="fa-stack" style="\n            height: 26px;\n            width: 30px;\n            display: inline-block;\n            height: 2em;\n            line-height: 2em;\n            position: relative;\n            vertical-align: middle;\n            width: 2.5em;">\n          <i class="fal fa-table fa-stack-1x"\n            style="font-size:16px; color:#9c9c9c; width:30px; top:-1px; left:0px;"></i>\n          <i class="fas fa-sort-down fa-stack-1x fa-inverse" style="\n              font-size: 14px;\n              top: -11px;\n              left: -5px;\n              width: 30px;"></i>\n        </span>\n      </button>\n      <button class=\'btn btn-small btn-lightgrey btnDataFrame nodisplay\' rel=\'tooltip\'\n        data-original-title=\''+s(i(n(668)).call(l,"_group",{name:"L",hash:{},data:r,loc:{start:{line:55,column:29},end:{line:55,column:43}}}))+"/"+s(i(n(668)).call(l,"aggregate",{name:"L",hash:{},data:r,loc:{start:{line:55,column:44},end:{line:55,column:61}}}))+"' data-action='wiz-dataframe-groupby'>\n        <i class=\"fal fa-layer-group\"></i>\n      </button>\n      <button class='btn btn-small btn-lightgrey btnDataFrame nodisplay' rel='tooltip'\n        data-original-title='"+s(i(n(668)).call(l,"_create_index",{name:"L",hash:{},data:r,loc:{start:{line:59,column:29},end:{line:59,column:50}}}))+"' data-action='wiz-dataframe-index-from-pandas'>\n        <i class=\"fal fa-bookmark\"></i>\n      </button>\n      <button class='btn btn-small btn-lightgrey btnDataFrame nodisplay' rel='tooltip'\n        data-original-title='"+s(i(n(668)).call(l,"create_dataarray",{name:"L",hash:{},data:r,loc:{start:{line:63,column:29},end:{line:63,column:53}}}))+"' data-action='wiz-dataarray-from-pandas'>\n        <i class=\"fal fa-cube\"></i>\n      </button>\n      <button class='btn btn-small btn-lightgrey btnInputTable nodisplay' rel='tooltip'\n        data-original-title='"+s(i(n(668)).call(l,"edit_inputTable",{name:"L",hash:{},data:r,loc:{start:{line:67,column:29},end:{line:67,column:52}}}))+"' data-action='wiz-inputtable'>\n        <i class=\"far fa-table\"></i>\n      </button>\n      <button class='btn btn-small btn-lightgrey btnDataArray nodisplay' rel='tooltip'\n        data-original-title='"+s(i(n(668)).call(l,"filter",{name:"L",hash:{},data:r,loc:{start:{line:71,column:29},end:{line:71,column:43}}}))+"' data-action='wiz-dataarray-filter'>\n        <i class=\"far fa-filter\"></i>\n      </button>\n\n\n      <button class='btn btn-small btn-lightgrey btnIndex nodisplay' rel='tooltip'\n        data-original-title='"+s(i(n(668)).call(l,"_edit_index",{name:"L",hash:{},data:r,loc:{start:{line:77,column:29},end:{line:77,column:48}}}))+'\' data-action=\'wiz-edit-index\' style="height:26px; padding:0">\n        <span class="fa-stack" style="\n            height: 26px;\n            width: 30px;\n            display: inline-block;\n            height: 2em;\n            line-height: 2em;\n            position: relative;\n            vertical-align: middle;\n            width: 2.5em;">\n          <i class="far fa-bars fa-stack-1x" style="font-size:16px; color:#9c9c9c; width:30px; top:-1px; left:0px;"></i>\n          <i class="fas fa-pencil fa-stack-1x fa-inverse" style="\n              font-size: 11px;\n              top: 1px;\n              left: 3px;\n              width: 30px;\n              "></i>\n        </span>\n      </button>\n      <button class=\'btn btn-small btn-lightgrey btnIndex nodisplay\' rel=\'tooltip\'\n        data-original-title=\''+s(i(n(668)).call(l,"_rename_index_item",{name:"L",hash:{},data:r,loc:{start:{line:97,column:29},end:{line:97,column:55}}}))+"' data-action='wiz-rename-index-item'>\n        <i class=\"far fa-tag\"></i>\n      </button>\n      <button class='btn btn-small btn-lightgrey btnCopyAsValues nodisplay' rel='tooltip'\n        data-original-title='"+s(i(n(668)).call(l,"_copy_as_values",{name:"L",hash:{},data:r,loc:{start:{line:101,column:29},end:{line:101,column:52}}}))+'\' data-action=\'wiz-copyasvalues\' style="height:26px; padding:0">\n        <span class="fa-stack" style="\n            height: 26px;\n            width: 30px;\n            display: inline-block;\n            height: 2em;\n            line-height: 2em;\n            position: relative;\n            vertical-align: middle;\n            width: 2.5em;">\n          <i class="far fa-clipboard fa-stack-1x" style="font-size:16px; width:30px; top:-1px; left:-2px;"></i>\n          <strong class="fa-stack-1x" style="\n            font-size: 7px;\n            left: 12px;\n            top: 11px;\n            font-weight: 100;\n            width: 13px;\n            height: 8px;\n            background-color: #fff;\n            color: #333;\n            line-height: 1.3em;\n            letter-spacing: 0px;">123</strong>\n        </span>\n      </button>\n\n    </div>\n    <div class=\'resultArea row\'>\n      <div class=\'col-sm-12 atomic nodisplay\' style="padding: 0;">\n        <pre class=\'resultPreview\'></pre>\n      </div>\n    </div>\n  </div>\n</div>'},useData:!0})},767:function(e,a,n){"use strict";(function(t){var i,o=n(679);void 0===(i=function(){return t.Model.extend({url:"knowledgeBase",getPost:function(e,a){(0,o.send)("KnowledgeBase/getPost?nodeId="+e,null,{type:"GET"},a)},search:function(e,a){(0,o.send)("KnowledgeBase/search",e,{type:"POST"},a)},generatePost:function(e,a){(0,o.send)("KnowledgeBase/generatePost?nodeId="+e,null,{type:"POST"},a)},updatePost:function(e,a){(0,o.send)("KnowledgeBase/updatePost",e,{type:"PUT"},a)},deleteAttachedFile:function(e,a){(0,o.send)("KnowledgeBase/deleteDocument?url="+e,null,{type:"DELETE"},a)}})}.apply(a,[]))||(e.exports=i)}).call(this,n(219))}}]);
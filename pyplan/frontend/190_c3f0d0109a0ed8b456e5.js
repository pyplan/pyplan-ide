/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[190],{1053:function(e,t,i){var s=i(690);function r(e){return e&&(e.__esModule?e.default:e)}e.exports=(s.default||s).template({compiler:[7,">= 4.0.0"],main:function(e,t,s,a,n){var o=null!=t?t:e.nullContext||{},l=e.escapeExpression;return'\n<div class="nodetable">\n\n    \x3c!-- <button class="btn btn-mini btn-primary toggle-mode toolbar-area result-mode"> '+l(r(i(688)).call(o,"result",{name:"L",hash:{},data:n}))+'</button>\n    <button class="btn btn-mini toggle-mode toolbar-area edit-mode"> '+l(r(i(688)).call(o,"edit",{name:"L",hash:{},data:n}))+'</button> --\x3e\n\n    \x3c!--div class="changes-area" >\n      <span class="pending-changes">0</span>\n      <span class="pending-changes-text"> '+l(r(i(688)).call(o,"uncommited_changes",{name:"L",hash:{},data:n}))+' </span>\n\n      <button class="btn btn-satgreen btn-mini btn--icon applyChanges"><i class="fa fa-check"></i>'+l(r(i(688)).call(o,"_apply",{name:"L",hash:{},data:n}))+'</button>\n      <button class="btn btn-lightred btn-mini btn--icon cancelChanges"><i class="fa fa-remove"></i>'+l(r(i(688)).call(o,"cancel",{name:"L",hash:{},data:n}))+'</button>\n\n    </div--\x3e\n\n\n    <div class="nodetable-area">\n\n    </div>\n\n</div>\n'},useData:!0})},931:function(e,t,i){"use strict";(function(s,r){var a,n,o=i(18);a=[i(723),i(963),i(965),i(1053)],void 0===(n=function(e,t,a,n){return e.extend({el:s("#n_o_n_e"),pivotTable:void 0,pivotModel:void 0,currentMode:"result",lastScaleFactor:1,lastSyncField:void 0,forceReloadMenu:!0,scrollToRight:!1,scrollToBottom:!1,changeOfScenario:!1,render:function(e){this.baseRender(e),s(this.tagId).find("div[data-rel='exports']").hide(),s(this.tagId).find("div.detail-area").remove(),this.drawItem()},updateSize:function(e,t,i){var r=this;setTimeout(function(){void 0!=r.pivotTable&&s(r.tagId).length>0&&(r.lastScaleFactor!=r.maxScaleFactorW&&r.applyScaleFactor(),r.pivotTable.updateSize())},200)},onRemoveItemView:function(){if(this.pivotTable)try{this.pivotTable.destroy()}catch(e){}this.pivotTable=null},refreshItemDash:function(){!this.changeOfScenario&&this.pivotTable?(this.pivotTable.clearChanges(),this.refreshApplyChanges(),this.loadCubeData()):this.drawTable(),this.changeOfScenario=!1},onFilterChange:function(e,t,i,s,r){var a=this.getIndexByField(e);a&&(e=a.field,this.pivotTable&&e!=this.lastSyncField&&(this.isUnlinkedIndex(e)||this.pivotTable.syncExternalFilter(e,t)))},onFiltersChange:function(e){for(var t=!1,i=0;i<e.length;i++){var s=e[i].field;if(this.getIndexByField(s)&&!this.isUnlinkedIndex(s)){t=!0;break}}t&&this.pivotTable&&this.pivotTable.onFiltersChange(e)},needRefresh:function(e){return!!(e&&e.indexOf(this.currentNodeId)>=0)},getOptionsMenu:function(){var e=this,t="far fa-square",i="far fa-square";e.currentResult&&e.currentResult.itemProperties&&(e.currentResult.itemProperties.showColumnTotal&&(i="fa fa-check-square"),e.currentResult.itemProperties.showRowTotal&&(t="fa fa-check-square"));var r={callback:function(t){switch(t){case"_full":e.fullScreen();break;case"_hideFilter":s(e.tagId).find(".pivotAreaFilter").toggleClass("hideZone"),i=!s(e.tagId).find(".pivotAreaFilter").hasClass("hideZone"),e.setViewToggleDetail(i);break;case"_knowledge":e.openDocumentationModal();break;case"_workflow":e.addTask();break;case"_view_in_diagram":e.viewInDiagram();break;case"_export":e.exportItem();break;case"_columnTotal":var i=!0;e.currentResult&&e.currentResult.itemProperties&&(i=!e.currentResult.itemProperties.showColumnTotal),e.setShowColumnTotal(i);break;case"_rowTotal":i=!0;e.currentResult&&e.currentResult.itemProperties&&(i=!e.currentResult.itemProperties.showRowTotal),e.setShowRowTotal(i)}},items:{_full:{type:"icon_text",name:(0,o.translate)("fullscreen"),iconClass:"fa fa-expand"},_hideFilter:{type:"icon_text",name:(0,o.translate)("view_detail"),iconClass:"fa fa-filter"},sep1:"---------",_columnTotal:{type:"icon_text",name:(0,o.translate)("menu_column_total"),iconClass:i,persist:!1},_rowTotal:{type:"icon_text",name:(0,o.translate)("menu_row_total"),iconClass:t,persist:!1},sep2:"---------",_export:{type:"icon_text",name:(0,o.translate)("_export"),iconClass:"fa fa-download"},sep3:"---------"}};return r.items._knowledge={type:"icon_text",name:(0,o.translate)("documentation"),iconClass:"fa fa-graduation-cap"},(0,o.haveAnyAccess)("LISTASSIGNEDWORKFLOWTASKS,LISTALLWORKFLOWTASKS")&&(r.items._workflow={type:"icon_text",name:(0,o.translate)("workflow"),iconClass:"fa fa-tasks"}),(0,o.haveAccess)("view_influence_diagram")&&(r.items._view_in_diagram={type:"icon_text",name:(0,o.translate)("view_in_diagram"),iconClass:"fa fa-sitemap"}),e.fromEmbedded&&(delete r.items.sep2,delete r.items._splitBy,delete r.items._knowledge,delete r.items._workflow,delete r.items._view_in_diagram),r},setViewToggleDetail:function(e){e?s(this.tagId).find(".pivotAreaFilter").removeClass("hideZone"):s(this.tagId).find(".pivotAreaFilter").addClass("hideZone"),this.currentResult&&this.currentResult.itemProperties&&(this.currentResult.itemProperties.detail=e),this.updateSize()},setViewDetail:function(e){e?s(this.tagId).find(".pivotAreaFilter").removeClass("hideZone"):s(this.tagId).find(".pivotAreaFilter").addClass("hideZone"),this.currentResult&&this.currentResult.itemProperties&&(this.currentResult.itemProperties.detail=e),this.updateSize()},addTask:function(){var e=this;i.e(9).then(function(){var t=[i(704)];(function(t){(new t).showAddTaskForNode(e.currentNodeId)}).apply(null,t)}).catch(i.oe)},_evaluateNode:function(e,t,i,s,r,a){},updateValues:function(e){},drawItem:function(){var e=n();s(this.tagId).find(".item-area").empty(),s(this.tagId).find(".item-area").html(e),s(this.tagId).find(".changes-area").hide(),this.model&&this.model.attributes&&this.model.attributes.extraOptions&&this.model.attributes.extraOptions.isInputNode&&(this.setDefaultOptions(),this.currentResult.itemProperties.cubeOptions.editMode=!0),this.currentResult&&this.currentResult.itemProperties&&this.currentResult.itemProperties.cubeOptions&&this.currentResult.itemProperties.cubeOptions.editMode&&(this.currentMode="edit",s(this.tagId).find(".toggle-mode").removeClass("btn-primary"),s(this.tagId).find(".toggle-mode.edit-mode").addClass("btn-primary"),s(this.tagId).find(".toggle-mode").addClass("editMode"),s(this.tagId).find(".toggle-mode").attr("title",(0,o.translate)("edit"))),this.addHandlers(),this.drawTable(),this.updateSize()},applyScaleFactor:function(){this.lastScaleFactor=this.maxScaleFactorW,s(this.tagId).find(".item-area").css("font-size",11*this.maxScaleFactorW+"px")},drawTable:function(){this.applyScaleFactor(),this.pivotModel=new a;var e,i=this;this.setDefaultOptions(),this.currentResult&&this.currentResult.nodeId&&(this.currentResult.itemProperties.cubeOptions.nodeId=this.currentResult.nodeId,e=this.currentResult.nodeId);var r={cube:e,mode:this.currentMode};this.pivotModel.getCubeMetadata(r,function(e){e&&e.isEditable&&!i.fromEmbedded?s(i.tagId).find(".toolbar-area").show():s(i.tagId).find(".toolbar-area").hide(),i.pivotTable=new t,i.pivotTable.setElement(s(i.tagId).find(".item-area")),__currentSession&&__currentSession.modelInfo?(i.pivotTable.remoteMode(!0),i.pivotTable.olapMode(!0),i.pivotTable.setMetadata(e),i.updatePropertiesOnEvaluate(e),i.pivotTable.setRemoteCallbacks({queryTable:function(e){i.queryTable(e)},queryDimension:function(e,t){i.queryDimension(e,t)}}),i.loadCubeData()):(i.pivotTable.remoteMode(!1),i.pivotTable.setMetadata(e),i.updatePropertiesOnEvaluate(e),i.loadCubeData()),i.currentResult.itemProperties.detail?s(i.tagId).find(".pivotAreaFilter").removeClass("hideZone"):s(i.tagId).find(".pivotAreaFilter").addClass("hideZone")},function(){i.isReady=!0})},loadCubeData:function(){var e,t=this,i=this.currentResult.nodeId,r=this.currentResult.itemProperties.cubeOptions.editMode;this.currentResult&&this.currentResult.itemProperties&&this.currentResult.itemProperties.numberFormat&&(this.numberFormat=this.currentResult.itemProperties.numberFormat);try{this.ensureDims(this.currentResult.itemProperties.cubeOptions,this.pivotTable.metadata)}catch(e){}try{this.ensureMeasures(this.currentResult.itemProperties.cubeOptions,this.pivotTable.metadata)}catch(e){}var a=function(e,t){return!isNaN(parseFloat(t))&&(parseFloat(t)>=parseFloat(e.from)&&parseFloat(t)<parseFloat(e.to))};this.currentResult&&this.currentResult.itemProperties&&this.currentResult.itemProperties.validation&&this.currentResult.itemProperties.validation.styleLibrary&&(e=this.model.getStyleLibrary(this.currentResult.itemProperties.validation.styleLibrary));var n=!0,o=!0;this.pivotTable&&this.pivotTable.metadata&&this.pivotTable.metadata.measures&&this.pivotTable.metadata.measures.length>0&&(o=!1,this.pivotTable.metadata.measures.length>1&&(n=!1));var l=s.extend({hideOptionsArea:n,hideRenderersArea:o,editMode:!1,rendererName:"Pivot Table",cubename:i,rows:[],cols:[],onDrawTable:function(e){t.updateProperties(e),setTimeout(function(){t.autoScrollOnTotal()},50),t.isReady=!0},onEdit:function(e,i){t.refreshApplyChanges()},onFilter:function(e,i){t.syncFilters(e,i)},getValidationStyle:function(t){if(e)for(var i=0;i<e.length;i++)if(t&&a(e[i],t))return e[i]}},t.currentResult.itemProperties.cubeOptions);if(l.editMode=r,l.rendererName=r?"Input Table":l.rendererName,l.aggregator=r?"listUnique":"genericSum",l.numberFormat=this.numberFormat,t.pivotTable.setOptions(l),__currentSession&&__currentSession.modelInfo)t.pivotTable.forceQuery=!0,t.pivotTable.refreshTable();else{var u={cube:i,mode:this.currentMode};this.currentResult&&this.currentResult.itemProperties&&this.currentResult.itemProperties.validation&&this.currentResult.itemProperties.validation.node&&(u.validationNode=this.currentResult.itemProperties.validation.node),this.showLoading(),this.pivotModel.getCubeValues(u,function(e){t.hideLoading(),t.pivotTable.setCubedata(e),void 0===t.currentResult.itemProperties.showRowTotal&&(t.currentResult.itemProperties.showRowTotal=!1),void 0===t.currentResult.itemProperties.showColumnTotal&&(t.currentResult.itemProperties.showColumnTotal=!1),t.pivotTable.drawTable(t.currentResult.itemProperties),t.currentResult.itemProperties.detail?s(t.tagId).find(".pivotAreaFilter").removeClass("hideZone"):s(t.tagId).find(".pivotAreaFilter").addClass("hideZone")},function(){t.hideLoading(),t.isReady=!0})}},setDefaultOptions:function(){this.currentResult.itemProperties?this.currentResult.itemProperties.cubeOptions||(this.currentResult.itemProperties.cubeOptions={}):this.currentResult.itemProperties={cubeOptions:{}},this.currentResult.itemProperties.validation||(this.currentResult.itemProperties.validation={})},updateProperties:function(e){e&&(this.setDefaultOptions(),this.currentResult.itemProperties.cubeOptions.rows=e.rows,this.currentResult.itemProperties.cubeOptions.cols=e.cols,this.currentResult.itemProperties.cubeOptions.aggregator=e.aggregator,this.currentResult.itemProperties.cubeOptions.rendererName=e.rendererName,this.currentResult.itemProperties.cubeOptions.filters=e.filters,this.currentResult.itemProperties.cubeOptions.positionFilters=e.positionFilters,e.selectedMeasures&&(this.currentResult.itemProperties.cubeOptions.selectedMeasures=e.selectedMeasures))},refreshApplyChanges:function(){if(s(this.tagId).find(".changes-area").hide(),this.pivotTable){this.pivotTable.metadata&&this.pivotTable.metadata.isEditable&&!this.fromEmbedded?s(this.tagId).find(".toolbar-area").show():s(this.tagId).find(".toolbar-area").hide();var e=this.pivotTable.getUncommittedChanges();e&&e.length>0&&(s(this.tagId).find(".changes-area .pending-changes").html(e.length),s(this.tagId).find(".changes-area").show(),s(this.tagId).find(".toolbar-area").hide())}},addHandlers:function(){var e=this;s(this.tagId).find(".changes-area .applyChanges").on("click",function(){var t={node:e.currentResult.nodeId,changes:e.pivotTable.getUncommittedChanges()};e.showLoading(),e.pivotModel.setCubeChanges(t,function(t){e.pivotTable.clearChanges(),e.refreshApplyChanges(),e.hideLoading(),e.model.reevaluateNodesNeeded(e.tagId);s("#nodePropertiesDock").trigger("refreshNodeDefinition",[e.currentNodeId,!0]),e.currentResult&&e.currentResult.itemProperties&&e.currentResult.itemProperties.validation&&e.currentResult.itemProperties.validation.node&&e.loadCubeData()},function(t){e.hideLoading()})}),s(this.tagId).find(".changes-area .cancelChanges").on("click",function(){s(e.tagId).find(".changes-area .pending-changes").html(0),e.pivotTable.clearChanges(),e.refreshApplyChanges(),e.loadCubeData()}),s(this.tagId).find(".toggle-mode").on("click",function(){e.setDefaultOptions(),s(e.tagId).find(".toggle-mode").toggleClass("editMode"),s(this).hasClass("editMode")?(e.currentResult.itemProperties.cubeOptions.editMode=!0,e.currentMode="edit",s(this).attr("title",(0,o.translate)("result"))):(e.currentResult.itemProperties.cubeOptions.editMode=!1,e.currentMode="result",s(this).attr("title",(0,o.translate)("edit"))),e.pivotTable&&e.pivotTable.destroy(),e.drawTable()}),s(this.tagId).closest(".mainTask").on("scenarioUnloaded",function(){if(e.changeOfScenario=!0,e.currentResult&&e.currentResult.itemProperties&&e.currentResult.itemProperties.cubeOptions){if(e.currentResult.itemProperties.cubeOptions.rows)for(var t=0;t<e.currentResult.itemProperties.cubeOptions.rows.length;t++)if(e.currentResult.itemProperties.cubeOptions.rows[t].toLocaleLowerCase().indexOf(".scenario")>=0){e.currentResult.itemProperties.cubeOptions.rows.splice(t,1);break}if(e.currentResult.itemProperties.cubeOptions.cols)for(t=0;t<e.currentResult.itemProperties.cubeOptions.cols.length;t++)if(e.currentResult.itemProperties.cubeOptions.cols[t].toLocaleLowerCase().indexOf(".scenario")>=0){e.currentResult.itemProperties.cubeOptions.cols.splice(t,1);break}}}),s(this.tagId).closest(".mainTask").on("scenarioLoaded",function(){e.changeOfScenario=!0})},applyNumberFormat:function(){this.refreshItemDash()},syncFilters:function(e,t){var i=t,r=[];if(e&&e.filters)for(var a in e.filters)i=a,e.filters[a].values&&s.each(e.filters[a].values,function(e,t){r.push({selected:!0,value:t})});i&&(this.lastSyncField=i,this.model.onFilterChange(i,r,void 0,void 0,this.tagId,500),this.lastSyncField="")},setShowRowTotal:function(e){this.currentResult.itemProperties.showRowTotal=e,this.scrollToBottom=!0,this.refreshItemDash()},setShowColumnTotal:function(e){this.currentResult.itemProperties.showColumnTotal=e,this.scrollToRight=e,this.refreshItemDash()},setIndexEvent:function(e,t){this.currentResult.itemProperties.indexEvents||(this.currentResult.itemProperties.indexEvents={}),t?delete this.currentResult.itemProperties.indexEvents[e]:this.currentResult.itemProperties.indexEvents[e]=!0},autoScrollOnTotal:function(){this.pivotTable&&this.pivotTable.htTable&&((this.scrollToBottom||this.scrollToRight)&&this.pivotTable.htTable.scrollViewportTo(this.pivotTable.htTable.countRows()-1,this.pivotTable.htTable.countCols()-1),this.scrollToBottom=!1,this.scrollToRight=!1)},ensureDims:function(e,t){if(t&&t.dims&&e){var i=function(e){for(var i=0;i<t.dims.length;i++)if(t.dims[i].field==e)return!0;return!1};if(e.cols&&e.cols.length>0)for(var s=e.cols.length-1;s>=0;s--)i(e.cols[s])||e.cols.splice(s,1);if(e.rows&&e.rows.length>0)for(s=e.rows.length-1;s>=0;s--)i(e.rows[s])||e.rows.splice(s,1)}},ensureMeasures:function(e,t){if(t&&t.measures&&e){var i=function(e){for(var i=0;i<t.measures.length;i++)if(t.measures[i].field==e)return!0;return!1};if(e.selectedMeasures&&e.selectedMeasures.length>0)for(var s=e.selectedMeasures.length-1;s>=0;s--)i(e.selectedMeasures[s])||e.selectedMeasures.splice(s,1)}},setValidationNode:function(e){this.currentResult.itemProperties.validation.node=e,this.refreshItemDash()},setValidationStyleLib:function(e){this.currentResult.itemProperties.validation.styleLibrary=e,this.pivotTable&&this.pivotTable.destroy(),this.drawTable()},queryTable:function(e){this.showLoading();var t=this;this.pivotModel.getCubeValues(e,function(e){t.hideLoading(),t.pivotTable.setCubedata(e),void 0===t.currentResult.itemProperties.showRowTotal&&(t.currentResult.itemProperties.showRowTotal=!1),void 0===t.currentResult.itemProperties.showColumnTotal&&(t.currentResult.itemProperties.showColumnTotal=!1),t.pivotTable.drawTable(t.currentResult.itemProperties),t.currentResult.itemProperties.detail?s(t.tagId).find(".pivotAreaFilter").removeClass("hideZone"):s(t.tagId).find(".pivotAreaFilter").addClass("hideZone")},function(){t.hideLoading(),t.isReady=!0})},queryDimension:function(e,t){this.pivotModel.getDimensionValues(e,function(e){t(e)})},exportItem:function(){var e,t=this.currentNodeId;this.currentResult.itemProperties&&(e=this.currentResult.itemProperties.summaryBy);var a=(this.currentResult.dims,this.currentResult.rows,this.currentResult.columns),n=this;a={current_selection_callback:function(e,t,i,a,o){var l=n.pivotTable.htTable,u=!1;"TSPDSC"==i&&(u=!0);var c="\t";"tab"!=a&&(c=a);var d=-1;n.currentResult&&n.currentResult.itemProperties&&n.currentResult.itemProperties.cubeOptions&&n.currentResult.itemProperties.cubeOptions.rows&&n.currentResult.itemProperties.cubeOptions.rows.length>0&&n.currentResult.itemProperties.cubeOptions.cols&&n.currentResult.itemProperties.cubeOptions.cols.length>0&&(d=n.currentResult.itemProperties.cubeOptions.rows.length);var h=[];h.push("data:text/csv;charset=utf-8,"),r.each(l.getData(),function(e,t){h.push(function(e,t){var i="";return r.each(e,function(e,t){d!=t&&(e&&"string"==typeof e&&e.indexOf("connectedDimsSortable")>=0?(e=s(e).find("span.name").text())&&(e=e.substr(0,e.length-1)):u&&"number"==typeof e&&(e=(e=String(e).replace(".","_")).replace("_",",")),i+=(r.contains(e,c)?'"'+e+'"':e)+c)}),i=i.substr(0,i.length-1)+"\n"}(e))});var p=h.join("");o(encodeURI(p)),n=null}},i.e(3).then(function(){var e=[i(699)];(function(e){(new e).exportNode(t,a)}).apply(null,e)}).catch(i.oe)}})}.apply(t,a))||(e.exports=n)}).call(this,i(1),i(220))}}]);
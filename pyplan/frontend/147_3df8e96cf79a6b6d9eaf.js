/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[147],{1155:function(e,t,i){var n=i(670);function r(e){return e&&(e.__esModule?e.default:e)}e.exports=(n.default||n).template({1:function(e,t,i,n,r){return" mini "},3:function(e,t,i,n,r){return" orientation-vertical "},5:function(e,t,i,n,r){return"             \n"},7:function(e,t,n,l,s){return'            <li class="selectAll">'+e.escapeExpression(r(i(668)).call(null!=t?t:e.nullContext||{},"All",{name:"L",hash:{},data:s,loc:{start:{line:7,column:34},end:{line:7,column:45}}}))+"</li>\n"},9:function(e,t,n,l,s){var a,u=e.lambda,d=e.escapeExpression,c=e.lookupProperty||function(e,t){if(Object.prototype.hasOwnProperty.call(e,t))return e[t]};return'            <li data-value="'+d(u(null!=t?c(t,"value"):t,t))+'"  class="indexOption '+(null!=(a=r(i(669)).call(null!=t?t:e.nullContext||{},null!=t?c(t,"selected"):t,"==",!0,{name:"ifCond",hash:{},fn:e.program(10,s,0),inverse:e.noop,data:s,loc:{start:{line:10,column:59},end:{line:10,column:110}}}))?a:"")+'" >'+d(u(null!=t?c(t,"formattedValue"):t,t))+"</li>\n"},10:function(e,t,i,n,r){return" selected "},compiler:[8,">= 4.3.0"],main:function(e,t,n,l,s){var a,u=null!=t?t:e.nullContext||{},d=e.lookupProperty||function(e,t){if(Object.prototype.hasOwnProperty.call(e,t))return e[t]};return'<div class="index-list '+(null!=(a=r(i(669)).call(u,null!=(a=null!=(a=null!=t?d(t,"itemProperties"):t)?d(a,"index"):a)?d(a,"ui"):a,"==","mini",{name:"ifCond",hash:{},fn:e.program(1,s,0),inverse:e.noop,data:s,loc:{start:{line:1,column:23},end:{line:1,column:87}}}))?a:"")+" "+(null!=(a=r(i(669)).call(u,null!=(a=null!=(a=null!=t?d(t,"itemProperties"):t)?d(a,"index"):a)?d(a,"orientation"):a,"==","v",{name:"ifCond",hash:{},fn:e.program(3,s,0),inverse:e.noop,data:s,loc:{start:{line:1,column:88},end:{line:1,column:174}}}))?a:"")+'" node-id="'+e.escapeExpression(e.lambda(null!=(a=null!=t?d(t,"itemProperties"):t)?d(a,"nodeId"):a,t))+'">\n\n    <ul>\n'+(null!=(a=d(n,"if").call(u,null!=(a=null!=(a=null!=t?d(t,"itemProperties"):t)?d(a,"index"):a)?d(a,"singleSelect"):a,{name:"if",hash:{},fn:e.program(5,s,0),inverse:e.program(7,s,0),data:s,loc:{start:{line:4,column:8},end:{line:8,column:15}}}))?a:"")+(null!=(a=d(n,"each").call(u,null!=t?d(t,"indexValues"):t,{name:"each",hash:{},fn:e.program(9,s,0),inverse:e.noop,data:s,loc:{start:{line:9,column:8},end:{line:11,column:17}}}))?a:"")+"    </ul>\n    \n</div>"},useData:!0})},1156:function(e,t,i){var n=i(670);e.exports=(n.default||n).template({compiler:[8,">= 4.3.0"],main:function(e,t,n,r,l){return'<div class="index-hidden">\n    <a href="#" class="text" rel="tooltip"  title="">('+e.escapeExpression((s=i(668),s&&(s.__esModule?s.default:s)).call(null!=t?t:e.nullContext||{},"all",{name:"L",hash:{},data:l,loc:{start:{line:2,column:54},end:{line:2,column:65}}}))+")</a>\n</div>";var s},useData:!0})},1157:function(e,t,i){var n=i(670);e.exports=(n.default||n).template({compiler:[8,">= 4.3.0"],main:function(e,t,i,n,r){return'<div class="index-range">\n    <div class="range_slider"></div>\n    <span class="range_min"></span>\n    <span class="range_max"></span>\n\n    <span class="label_range_min"></span>\n    <span class="label_range_sep">-</span>\n    <span class="label_range_max"></span>\n</div>'},useData:!0})},695:function(e,t){e.exports=function(){return""}},998:function(e,t,i){"use strict";(function(n){var r,l,s=i(18);r=[i(717),i(695),i(1155),i(1156),i(1157)],void 0===(l=function(e,t,r,l,a){return e.extend({el:n("#n_o_n_e"),table:void 0,clickTimeout:{},relatedTimeout:-1,uiFormat:"default",currentSelectedValues:void 0,render:function(e){this.baseRender(e),this.drawItem()},updateSize:function(e,t,i){var r=n(this.tagId);if(r.find(".item-area ul").height(n(this.tagId).find(".item-area").height()-5),"hidden"==this.uiFormat){r.find(".item-title").width(),r.find(".item-title .unit").width();r.find(".item-area .index-hidden").css("rigth",0),r.find(".item-area .index-hidden a").width(n(this.tagId).width()-15)}if(r.find(".index-list").length>0){var l=Math.min(this.maxScaleFactorW,this.maxScaleFactorH),s=r.find(".index-list").hasClass("mini")?10:11;r.find(".index-list").css("font-size","".concat(s*l,"px"))}},updateValues:function(e){this.drawIndex(n(this.tagId).find(".item-area").first(),e),this.isReady=!0},drawItem:function(){var e=n(this.tagId),i=t();e.find(".item-area").html(i),this.currentResult&&this.currentResult.itemProperties&&this.currentResult.itemProperties.index&&(this.currentSelectedValues=this.currentResult.itemProperties.index.currentSelectedValues),this.drawIndex(e.find(".item-area").first())},redrawIndex:function(){this.drawIndex(n(this.tagId).find(".item-area").first(),this.currentResult)},drawIndex:function(e,t){var i=this;if(null==t&&this.currentResult&&(t=this.currentResult.nodeResult),t){var n=r;this.currentResult&&(this.currentResult.itemProperties&&this.currentResult.itemProperties.index&&this.currentResult.itemProperties.index.ui&&(this.uiFormat=this.currentResult.itemProperties.index.ui,"hidden"==this.currentResult.itemProperties.index.ui&&(n=l),"range"==this.currentResult.itemProperties.index.ui&&(n=a)),t.itemProperties=this.currentResult.itemProperties,t.itemProperties.nodeId=this.currentResult.nodeId,!t.indexValues&&this.currentResult.indexValues&&(t.indexValues=this.currentResult.indexValues)),this.numberFormatter||this.createFormatter(),t&&t.indexValues&&t.indexValues.forEach((function(e){e.formattedValue=i.numberFormatter?i.numberFormatter.format(e.value):e.value}));var s=n(t);e.html(s),this.addIndexEvents(),this.currentResult&&this.currentResult.itemProperties.index&&this.currentResult.itemProperties.index.dynamic?setTimeout((function(){i.refreshSettingChanges()}),50):(this.updateSelectedValues(),this.findAndQueryChildIndexes(),this.refreshSelectAll()),this.updateSize()}},addIndexEvents:function(){var e=this,t=n(this.tagId);switch(this.uiFormat){case"hidden":t.find(".index-hidden a").on("click",(function(){var n=e.currentNodeId,r=e.tagId,l=t.find(".item-title .title").text(),s=e.currentResult&&e.currentResult.itemProperties&&e.currentResult.itemProperties.index&&e.currentResult.itemProperties.index.singleSelect;return e.editMode||Promise.resolve().then((function(){var t=[i(687)];(function(t){(new t).getFilterView((function(t){var i=new t({singleSelect:s});i.setElement(),i.render(n,l,r,e)}))}).apply(null,t)})).catch(i.oe),!1}));break;case"range":if(this.currentResult&&this.currentResult.indexValues&&this.currentResult.indexValues.length>0){var r=n(this.tagId).find(".index-range .range_slider"),l=[];n(this.currentResult.indexValues).each((function(t,i){l.push(e.getTypedValue(i))})),r.hasClass(".ui-slider")&&r.slider("destroy"),r.slider({values:[0,l.length-1],range:!0,min:0,max:l.length-1,step:1,slide:function(i,n){t.find(".index-range  .label_range_min").text("(".concat(e.secureFormatValue(l[n.values[0]]))),t.find(".index-range  .label_range_max").text("".concat(e.secureFormatValue(l[n.values[1]]),")"))},stop:function(t,i){e.queryOnClick(!0)},create:function(i,n){t.find(".index-range .range_min").text(e.secureFormatValue(l[0])),t.find(".index-range .range_max").text(e.secureFormatValue(l[l.length-1])),t.find(".index-range .label_range_min").text("(".concat(e.secureFormatValue(l[0]))),t.find(".index-range .label_range_max").text("".concat(e.secureFormatValue(l[l.length-1]),")"))}})}break;default:t.find(".item-area .index-list ul li.indexOption").on("click",(function(i){e.setDefaultOptions();var r=i.target;e.currentResult.itemProperties.index.singleSelect&&n(r).closest("ul").find("li.indexOption").each((function(e,t){t!=r&&n(t).removeClass("selected")})),n(r).toggleClass("selected"),e.refreshSelectAll(),e.queryOnClick();var l=t.find(".item-area .index-list ul li.indexOption.selected"),s=[];l.each((function(e,t){s.push(n(t).attr("data-value"))})),n("[node-filter-id='".concat(e.currentResult.nodeId,"']")).trigger("dashboardIndexChange",[s])})),t.find(".item-area .index-list ul li.selectAll").on("click",(function(i){n(i.target).hasClass("selected")?n(i.target).closest("ul").find("li").removeClass("selected"):n(i.target).closest("ul").find("li").addClass("selected"),e.queryOnClick();var r=t.find(".item-area .index-list ul li.indexOption.selected"),l=[];r.each((function(e,t){l.push(n(t).attr("data-value"))})),n("[node-filter-id='".concat(e.currentResult.nodeId,"']")).trigger("dashboardIndexChange",[l,e.tagId])}))}},queryOnClick:function(e){var t=this,i=n(this.tagId),r=[];if("range"==this.uiFormat){var l=i.find(".index-range .range_slider"),s=l.slider("values",0),a=l.slider("values",1);n(this.currentResult.indexValues).each((function(e,t){e>=s&&e<=a&&r.push(t.value)}))}else i.find(".item-area ul li.indexOption.selected").each((function(e,t){r.push(n(t).attr("data-value"))}));if(this.currentResult){var u=this.currentResult.nodeId,d=this.currentResult&&this.currentResult.itemProperties.index&&this.currentResult.itemProperties.index.dynamic,c=[];r.forEach((function(e){c.push({selected:!0,value:e})}));var o=this.findAndQueryChildIndexes();clearTimeout(this.clickTimeout),this.clickTimeout=setTimeout((function(){t.model.onFilterChange(u,c,d,o)}),400)}},onFilterChange:function(e,t,i,n){var r=this;if(this.currentResult&&this.currentNodeId){var l=!1;e==this.currentNodeId&&(l=!0,this.currentSelectedValues=[],t&&t.forEach((function(e){e.selected&&r.currentSelectedValues.push(e.value)}))),this.updateSelectedValues(l),this.currentResult&&this.currentResult.itemProperties&&this.currentResult.itemProperties.index&&(this.currentResult.itemProperties.index.currentSelectedValues=this.currentSelectedValues),this.checkForRange()}},updateSelectedValues:function(e){var t=this,i=n(this.tagId);if((e||this.currentSelectedValues&&this.currentSelectedValues.length>0)&&this.currentSelectedValues)switch(this.uiFormat){case"hidden":var r="",l="",a=-1;this.currentResult&&this.currentResult.indexValues&&(a=this.currentResult.indexValues.length),this.currentSelectedValues&&0!=this.currentSelectedValues.length&&this.currentSelectedValues.length!=a?(this.currentSelectedValues.forEach((function(e,t){l+=t>0?",".concat(e):e})),r=l,this.currentSelectedValues.length>50&&(r=(0,s.translate)("multiple"))):r=(0,s.translate)("all"),r="(".concat(r,")"),i.find(".item-area .index-hidden a").text(r).attr("title",l);break;case"range":if(this.currentResult&&this.currentResult.indexValues&&this.currentResult.indexValues.length>0){var u,d,c,o,h=i.find(".index-range .range_slider");this.currentSelectedValues&&this.currentSelectedValues.length>0?n(this.currentResult.indexValues).each((function(e,i){i.value==t.currentSelectedValues[0]&&(c=t.getTypedValue(i),u=e),i.value==t.currentSelectedValues[t.currentSelectedValues.length-1]&&(o=t.getTypedValue(i),d=e)})):(u=0,d=this.currentResult.indexValues.length-1,c=this.getTypedValue(this.currentResult.indexValues[u]),o=this.getTypedValue(this.currentResult.indexValues[d].value)),h.slider("values",0,u),h.slider("values",1,d),i.find(".index-range .label_range_min").text("(".concat(this.secureFormatValue(c))),i.find(".index-range .label_range_max").text("".concat(this.secureFormatValue(o),")"))}break;default:i.find(".item-area ul li.indexOption").removeClass("selected"),this.currentSelectedValues.forEach((function(e){i.find(".item-area ul li.indexOption").each((function(t,i){n(i).attr("data-value")==e&&n(i).addClass("selected")}))})),this.refreshSelectAll()}},setSingleSelect:function(e){this.setDefaultOptions(),this.currentResult.itemProperties.index.singleSelect=e,e&&this.currentResult&&this.currentResult.indexValues&&this.currentResult.indexValues.length>0?this.currentSelectedValues=[this.currentResult.indexValues[0].value]:this.currentSelectedValues=[],this.redrawIndex(),this.queryOnClick(!0)},setUIFormat:function(e){this.setDefaultOptions(),this.currentResult.itemProperties.index.ui=e,this.redrawIndex()},setOrientation:function(e){this.setDefaultOptions(),this.currentResult.itemProperties.index.orientation=e,"v"==e?n(this.tagId).find(".index-list").addClass("orientation-vertical"):n(this.tagId).find(".index-list").removeClass("orientation-vertical")},setDynamic:function(e){this.setDefaultOptions(),!e&&this.currentResult.itemProperties.index.related&&(e=!0),this.currentResult.itemProperties.index.dynamic=e,this.refreshSettingChanges()},setRelated:function(e,t,i){this.setDefaultOptions(),this.currentResult.itemProperties.index.related=e,this.currentResult.itemProperties.index.related_index=void 0,e&&(this.currentResult.itemProperties.index.dynamic=e,this.currentResult.itemProperties.index.related_index=t,i&&(this.currentResult.itemProperties.index.related_table=i,n.each(this.model.getItemsModel(),(function(e,i){i.currentResult&&i.currentResult.nodeId==t&&i.queryOnClick(!0)}))))},setDefaultOptions:function(){this.currentResult.itemProperties.index||(this.currentResult.itemProperties.index={ui:"default",singleSelect:!1,orientation:"h",dynamic:!1,related:!1,related_index:void 0,related_table:void 0})},refreshSettingChanges:function(){var e=n(this.tagId);this.currentResult.itemProperties.index.singleSelect?(e.find(".item-area .index-list ul li.indexOption").removeClass("selected"),e.find(".item-area .index-list ul li.indexOption").first().addClass("selected")):(e.find(".item-area .index-list ul li.indexOption").addClass("selected"),e.find(".item-area .index-list ul li").first().removeClass("selected")),this.queryOnClick(!0),this.refreshSelectAll()},getRelatedNoQuery:function(){var e=[];if(this.currentResult&&this.currentResult.itemProperties.index&&this.currentResult.itemProperties.index.dynamic){var t=this;n.each(this.model.getItemsModel(),(function(i,r){var l=t.currentResult.nodeId;if(r.currentResult&&r.currentResult.dims&&r.currentResult.nodeId!=l){var s=!1;n.each(r.currentResult.dims,(function(e,t){t.field==l&&(s=!0)})),s||n.each(r.currentResult.rows,(function(e,t){t.field==l&&(s=!0)})),s||n.each(r.currentResult.columns,(function(e,t){t.field==l&&(s=!0)})),s&&e.push(r.currentResult.nodeId)}}))}return this.currentResult&&this.currentResult.itemProperties.index&&1==this.currentResult.itemProperties.index.related&&e.push(this.currentResult.nodeId),e},findAndQueryChildIndexes:function(){var e=!1,t=this.currentResult.nodeId,i=[];return n(this.tagId).find(".item-area .index-list ul li.indexOption.selected").each((function(e,t){i.push({selected:!0,value:n(t).attr("data-value")})})),n.each(this.model.getItemsModel(),(function(n,r){r.currentResult&&r.currentResult.nodeId!=t&&"indexlist"==r.currentResult.itemType&&r.currentResult.itemProperties&&r.currentResult.itemProperties.index&&1==r.currentResult.itemProperties.index.related&&r.currentResult.itemProperties.index.related_index==t&&(e=!0,r.queryRelatedTable(t,i))})),e},queryRelatedTable:function(e,t){var i=this;clearTimeout(this.relatedTimeout),this.relatedTimeout=setTimeout((function(){if(i.currentResult.itemProperties.index.related){var r=i.currentResult.itemProperties.index.related_table,l=[{field:e,name:e,values:t}],s={field:i.currentResult.nodeId,name:i.currentResult.nodeId,values:[]};i.model.evaluateNode(r,l,[s],[],(function(e){var t=[];n.each(e.series,(function(e,i){i.data&&i.data.length>0&&i.data[0]>0&&t.push({selected:!1,type:"S",value:i.name})}));var r={indexValues:t};i.updateValues(r),function(e){throw new Error('"'+e+'" is read-only')}("_this"),i=null}))}}),500)},refreshSelectAll:function(){var e=n(this.tagId).find(".item-area .index-list ul");e.find("li.indexOption").length==e.find("li.indexOption.selected").length?e.find("li.selectAll").addClass("selected"):e.find("li.selectAll").removeClass("selected")},getIndexByField:function(e){var t;if(e==this.currentNodeId){var i=[];this.currentSelectedValues&&this.currentSelectedValues.length>0&&this.currentSelectedValues.forEach((function(e){i.push({value:e,selected:!0})})),t={field:e,values:i}}return t},checkForRange:function(){if("range"==this.uiFormat&&this.currentResult&&this.currentResult.indexValues&&this.currentResult.indexValues.length>0&&this.currentSelectedValues&&this.currentSelectedValues.length>0){var e=this.currentSelectedValues[0],t=this.currentSelectedValues[this.currentSelectedValues.length-1],i=0,r=0;n(this.currentResult.indexValues).each((function(n,l){l.value==e&&(i=n),l.value==t&&(r=n)})),r-i+1>this.currentSelectedValues.length&&(this.currentResult.itemProperties.index.ui=this.uiFormat="default",this.redrawIndex())}},getTypedValue:function(e){return e?"N"==e.type?Number(e.value):e.value?e.value.toString():"":null},getOptionsMenu:function(){var e=this;this.currentResult&&this.currentResult.itemProperties&&(this.currentResult.itemProperties.rightTotal&&"fa fa-check-square",this.currentResult.itemProperties.bottomTotal);var t={callback:function(t){switch(t){case"_full":e.fullScreen();break;case"_knowledge":e.openDocumentationModal();break;case"_view_in_diagram":e.viewInDiagram()}},items:{_full:{type:"icon_text",name:(0,s.translate)("fullscreen"),iconClass:"fa fa-expand"},sep1:"---------"}};return t.items._knowledge={type:"icon_text",name:(0,s.translate)("documentation"),iconClass:"fa fa-graduation-cap"},(0,s.haveAccess)("view_influence_diagram")&&(t.items._view_in_diagram={type:"icon_text",name:(0,s.translate)("view_in_diagram"),iconClass:"fa fa-sitemap"}),this.fromEmbedded&&(delete t.items._knowledge,delete t.items._view_in_diagram),t}})}.apply(t,r))||(e.exports=l)}).call(this,i(1))}}]);
/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[192],{1079:function(e,t){e.exports=function(){return""}},1826:function(e,t,n){var i=n(690);e.exports=(i.default||i).template({1:function(e,t,n,i,l){return' multiple="multiple" style="width: 100%;" '},3:function(e,t,n,i,l){var a,r=e.lambda,s=e.escapeExpression;return'        <option value="'+s(r(null!=t?t.pos:t,t))+'" '+(null!=(a=n.if.call(null!=t?t:e.nullContext||{},null!=t?t.selected:t,{name:"if",hash:{},fn:e.program(4,l,0),inverse:e.noop,data:l,loc:{start:{line:4,column:32},end:{line:4,column:76}}}))?a:"")+">"+s(r(null!=t?t.value:t,t))+"</option>\n"},4:function(e,t,n,i,l){return' selected="selected" '},compiler:[8,">= 4.3.0"],main:function(e,t,i,l,a){var r,s=null!=t?t:e.nullContext||{};return'<div class="selector">\n    <select '+(null!=(r=function(e){return e&&(e.__esModule?e.default:e)}(n(689)).call(s,null!=(r=null!=t?t.itemProperties:t)?r.multiselect:r,"==","1",{name:"ifCond",hash:{},fn:e.program(1,a,0),inverse:e.noop,data:a,loc:{start:{line:2,column:12},end:{line:2,column:112}}}))?r:"")+">\n"+(null!=(r=i.each.call(s,null!=t?t.indexValues:t,{name:"each",hash:{},fn:e.program(3,a,0),inverse:e.noop,data:a,loc:{start:{line:3,column:8},end:{line:5,column:17}}}))?r:"")+"    </select>\n</div>"},useData:!0})},1827:function(e,t,n){var i=n(690);e.exports=(i.default||i).template({1:function(e,t,n,i,l){return" orientation-vertical "},3:function(e,t,n,i,l,a,r){var s,o=e.lambda,c=e.escapeExpression;return'        <li class="selector-item" style="position: relative; padding-left: 24px; padding-bottom: 0px;">\n            <input type="radio" id="'+c(o(l&&l.index,t))+"_"+c(o(null!=r[1]?r[1].tagId:r[1],t))+'" name="'+c(o(null!=r[1]?r[1].tagId:r[1],t))+'" value="'+c(o(null!=t?t.pos:t,t))+'" '+(null!=(s=n.if.call(null!=t?t:e.nullContext||{},null!=t?t.selected:t,{name:"if",hash:{},fn:e.program(4,l,0,a,r),inverse:e.noop,data:l,loc:{start:{line:5,column:97},end:{line:5,column:139}}}))?s:"")+' class="icheck-me" data-skin="square" data-color="'+c(o(null!=r[1]?r[1].customerColorSchema:r[1],t))+'" />\n            <label class="inline" for="'+c(o(l&&l.index,t))+"_"+c(o(null!=r[1]?r[1].tagId:r[1],t))+'">'+c(o(null!=t?t.formattedValue:t,t))+"</label>\n        </li>\n\n\n"},4:function(e,t,n,i,l){return' checked="checked" '},compiler:[8,">= 4.3.0"],main:function(e,t,i,l,a,r,s){var o,c=null!=t?t:e.nullContext||{};return'<div class="selector mini '+(null!=(o=function(e){return e&&(e.__esModule?e.default:e)}(n(689)).call(c,null!=(o=null!=t?t.itemProperties:t)?o.selectorOrientation:o,"==","v",{name:"ifCond",hash:{},fn:e.program(1,a,0,r,s),inverse:e.noop,data:a,loc:{start:{line:1,column:26},end:{line:1,column:114}}}))?o:"")+'">\n    <ul style="margin: 0; padding: 0;">\n'+(null!=(o=i.each.call(c,null!=t?t.indexValues:t,{name:"each",hash:{},fn:e.program(3,a,0,r,s),inverse:e.noop,data:a,loc:{start:{line:3,column:4},end:{line:10,column:13}}}))?o:"")+"</ul>\n    \n    \n</div>"},useData:!0,useDepths:!0})},1828:function(e,t,n){var i=n(690);e.exports=(i.default||i).template({compiler:[8,">= 4.3.0"],main:function(e,t,n,i,l){return'<div class="controls slider-container">\n  <div class="widget-slider selector-slider">\n    <div class="slide"></div>\n\n\n    <span class="range_min"></span>\n    <span class="range_max"></span>\n\n    <span class="label_range_min"></span>\n    <span class="label_range_sep">-</span>\n    <span class="label_range_max"></span>\n  </div>\n</div>'},useData:!0})},1829:function(e,t,n){var i=n(690);e.exports=(i.default||i).template({compiler:[8,">= 4.3.0"],main:function(e,t,n,i,l){return'<div class="controls slider-container">\n  <div class="widget-slider selector-slider">\n    <div class="slide"></div>\n\n\n    <span class="range_min"></span>\n    <span class="range_max"></span>\n\n    <span class="label_val"></span>\n  </div>\n</div>'},useData:!0})},1830:function(e,t,n){var i=n(690);e.exports=(i.default||i).template({1:function(e,t,n,i,l){return" orientation-vertical "},3:function(e,t,n,i,l,a,r){var s,o=e.lambda,c=e.escapeExpression;return'    <li class="selector-item" style="position: relative; padding-left: 5px; padding-bottom: 0px;">\n      <input type="checkbox" id="'+c(o(l&&l.index,t))+"_"+c(o(null!=r[1]?r[1].tagId:r[1],t))+'" name="'+c(o(null!=r[1]?r[1].tagId:r[1],t))+'" value="'+c(o(null!=t?t.pos:t,t))+'" '+(null!=(s=n.if.call(null!=t?t:e.nullContext||{},null!=t?t.selected:t,{name:"if",hash:{},fn:e.program(4,l,0,a,r),inverse:e.noop,data:l,loc:{start:{line:5,column:94},end:{line:6,column:33}}}))?s:"")+' class="icheck-me" data-skin="square" data-color="'+c(o(null!=r[1]?r[1].customerColorSchema:r[1],t))+'" />\n      <label class="inline" for="'+c(o(l&&l.index,t))+"_"+c(o(null!=r[1]?r[1].tagId:r[1],t))+'">'+c(o(null!=t?t.formattedValue:t,t))+"</label>\n    </li>\n"},4:function(e,t,n,i,l){return'\n        checked="checked" '},compiler:[8,">= 4.3.0"],main:function(e,t,i,l,a,r,s){var o,c=null!=t?t:e.nullContext||{};return'<div class="selector mini '+(null!=(o=function(e){return e&&(e.__esModule?e.default:e)}(n(689)).call(c,null!=(o=null!=t?t.itemProperties:t)?o.selectorOrientation:o,"==","v",{name:"ifCond",hash:{},fn:e.program(1,a,0,r,s),inverse:e.noop,data:a,loc:{start:{line:1,column:26},end:{line:1,column:114}}}))?o:"")+'">\n  <ul style="margin: 0; padding: 0;">\n'+(null!=(o=i.each.call(c,null!=t?t.indexValues:t,{name:"each",hash:{},fn:e.program(3,a,0,r,s),inverse:e.noop,data:a,loc:{start:{line:3,column:4},end:{line:9,column:13}}}))?o:"")+"  </ul>\n</div>"},useData:!0,useDepths:!0})},932:function(e,t,n){"use strict";(function(i){var l,a,r=n(18);function s(e){return(s="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}l=[n(720),n(1079),n(1826),n(1827),n(1828),n(1829),n(1830)],void 0===(a=function(e,t,l,a,o,c,u){return e.extend({el:i("#n_o_n_e"),currentDefinition:void 0,isSelector:!1,render:function(e){this.baseRender(e),this.drawItem()},drawItem:function(){var e=t();i(this.tagId).find(".item-area").html(e),i(this.tagId).find(".item-title").addClass("left"),i(this.tagId).find(".item-toolbar-view").hide(),this.fromEmbedded&&i(this.tagId).find(".btnMenu").hide(),this.drawSelector(),this.addGenericHandlers()},onRemoveItemView:function(){i(this.tagId).find(".item-area select").off("change"),i(this.tagId).find(".item-area input").off("change"),i(this.tagId).find("select").select2("destroy")},updateValues:function(e){this.currentResult&&(e.itemProperties=this.currentResult.itemProperties),this.drawSelector(e),this.isReady=!0},drawSelector:function(e){void 0==e&&this.currentResult&&(e=this.currentResult.nodeResult);var t,n=i(this.tagId).find(".item-area ").first(),s=!1,d=!1,f=!1,p=!1;if(e&&e.nodeProperties&&e.nodeProperties.isSelector?(this.isSelector=!0,this.currentResult.itemProperties.multiselect=e.nodeProperties.multiselect,p=e.nodeProperties.multiselect):e&&e.nodeProperties&&e.nodeProperties.isChoice&&(this.currentResult.itemProperties.multiselect=e.nodeProperties.multiselect,void 0==this.currentResult.itemProperties.multiselect&&(this.currentResult.itemProperties.multiselect=!1)),this.currentResult&&this.currentResult.itemProperties&&this.currentResult.itemProperties.selectorFormat)switch(this.currentResult.itemProperties.selectorFormat){case"options":t=a;break;case"slider":d=!0,t=c,"1"==p&&(this.currentResult.itemProperties.selectorFormat="range",t=o);break;case"range":d=!0,t=o,"0"==p&&(this.currentResult.itemProperties.selectorFormat="slider",t=c);break;case"multiCombo":t=l,s=!0;break;case"checkboxes":t=u,f=!0;break;default:t=l,s=!0}else t=l,s=!0,this.isSelector&&e.nodeProperties.multiselect;if(this.createFormatter(),e&&(e.nodeProperties&&(this.currentDefinition=e.nodeProperties.definition),e.tagId=this.tagId,e.indexValues)){for(var h=0;h<e.indexValues.length;h++)e.indexValues[h].pos=h,e.indexValues[h].formattedValue=e.indexValues[h].value,this.numberFormatter&&(e.indexValues[h].formattedValue=this.numberFormatter.format(e.indexValues[h].value));e.customerColorSchema=__customerStyles.customerColorSchema,f&&e.indexValues.unshift({pos:-1,value:"All",formattedValue:"All"})}n.find("select").select2("destroy");var m=t(e);if(n.html(m),(0,r.postRender)(n),s){var v=this,g=function(e){return v.numberFormatter&&!isNaN(parseFloat(e.text))?v.numberFormatter.format(e.text):e.text},k={width:"100%"};k.formatResult=g,k.formatSelection=g,k.escapeMarkup=function(e){return e},n.find("select").select2(k)}if(e&&d){v=this;var x=[],_=[],b=[];i.each(e.indexValues,function(e,t){x.push(t.formattedValue),t.selected&&_.push(t.pos)});var I=n.find(".widget-slider .slide");"1"===p?(b.push(Math.min.apply(null,_)),b.push(Math.max.apply(null,_)),I.slider({values:b,min:0,max:x.length-1,step:1,range:!0,slide:function(e,t){i(v.tagId).find(".label_range_min").text("("+x[t.values[0]]),i(v.tagId).find(".label_range_max").text(x[t.values[1]]+")")},stop:function(e,t){for(var n=t.values,i=[],l=n[0];l<=n[1];l++)i.push(l);v.updateSelectorDefinition(i)},create:function(e,t){i(v.tagId).find(".range_min").text(x[0]),i(v.tagId).find(".range_max").text(x[x.length-1]),i(v.tagId).find(".label_range_min").text("("+x[0]),i(v.tagId).find(".label_range_max").text(x[x.length-1]+")")}})):I.slider({value:_[0],min:0,max:x.length-1,step:1,slide:function(e,t){i(v.tagId).find(".label_val").text("("+x[t.value]+")")},stop:function(e,t){var n=t.value;v.updateSelectorDefinition(n)},create:function(e,t){i(v.tagId).find(".range_min").text(x[0]),i(v.tagId).find(".range_max").text(x[x.length-1]),i(v.tagId).find(".label_val").text("("+x[_[0]]+")")}})}},addGenericHandlers:function(){var e=this;i(this.tagId).find(".item-area").first().on("change",'select[multiple!="multiple"]',function(){var t=i(this).find("option:selected").text(),n=i(this).find("option:selected").index(),l=i(this).val();("all"==t||"All"==t)&&n>=i(this).find("option").length-1&&!e.isSelector&&(l=-1),e.updateSelectorDefinition(l)}),i(this.tagId).find(".item-area").first().on("select2-removing",'select[multiple="multiple"]',function(t){var n=i(this).find("option:selected").text(),l=i(this).find("option:selected").index(),a=i(this).val();if(("all"==n||"All"==n)&&l>=i(this).find("option").length-1&&!e.isSelector&&(a=-1),1==a.length)return t.preventDefault(),!1;e.updateSelectorDefinition(a)}).on("change",'select[multiple="multiple"]',function(t){var n=i(this).find("option:selected").text(),l=i(this).find("option:selected").index(),a=i(this).val();("all"==n||"All"==n)&&l>=i(this).find("option").length-1&&!e.isSelector&&(a=-1),e.updateSelectorDefinition(a)}),i(this.tagId).find(".item-area ").first().on("ifChecked",'input[type="radio"]',function(){var t=i(this).closest(".selector-item"),n=t.find("label").text(),l=t.index(),a=i(this).val();("all"==n||"All"==n)&&l>=i(this).closest(".selector").find(".selector-item").length-1&&!e.isSelector&&(a=-1),e.updateSelectorDefinition(a)}),i(this.tagId).find(".item-area").first().on("click","selector-item",function(){var e=i(this),t=i(e).closest(".item-area").find("input[value!=-1][checked=checked]").length;if("checked"===i(e).attr("checked")&&1==t)return event.stopImmediatePropagation(),!1}),i(this.tagId).find(".item-area").first().on("ifClicked",'input[type="checkbox"]',function(t){var n=this,l=i(this).closest(".item-area").find("input[type=checkbox]"),a=i(this),r=i(a).closest(".item-area").find("input[value!=-1][checked=checked]").length;setTimeout(function(){if("checked"===a.attr("checked")){if("checked"===i(a).attr("checked")&&1==r)return a.attr("checked","checked").iCheck("update"),a.iCheck("check").iCheck("update"),!1;a.removeAttr("checked").iCheck("update")}else a.attr("checked","checked").iCheck("update");"-1"==i(n).val()&&i.each(l,function(e,t){"checked"===i(a).attr("checked")?(i(t).iCheck("check").iCheck("update"),i(t).attr("checked","checked").iCheck("update")):e>1&&(i(t).iCheck("uncheck").iCheck("update"),i(t).removeAttr("checked").iCheck("update"))});var t=[],s=!0;i.each(l,function(e,n){"-1"!==i(n).val()&&("checked"===i(n).attr("checked")?t.push(i(n).val()):s=!1)}),s?(i(e.tagId).find("input[type=checkbox][value=-1]").attr("checked","checked").iCheck("update"),i(e.tagId).find("input[type=checkbox][value=-1]").iCheck("check").iCheck("update")):(i(e.tagId).find("input[type=checkbox][value=-1]").removeAttr("checked").iCheck("update"),i(e.tagId).find("input[type=checkbox][value=-1]").iCheck("uncheck").iCheck("update")),e.updateSelectorDefinition(t)},10)})},updateSelectorDefinition:function(e){if(this.currentDefinition&&""!=this.currentDefinition)if("object"==s(e)&&(e="["+e+"]"),this.isSelector){for(var t,n=/(?:[^\]\[,]+|\[[^\]\[]+\])+/gm,l=[];null!==(t=n.exec(this.currentDefinition));)t.index===n.lastIndex&&n.lastIndex++,t.forEach(function(e,t){l.push(e)});if(l.length>1){var a="".concat(l[0],",").concat(String(e));3==l.length&&(a="".concat(a,",").concat(l[2])),this.updateNodeDefinition(this.currentResult.nodeId,a),i("#nodePropertiesDock").trigger("refreshNodeDefinition",[this.currentResult.nodeId])}}else this.updateChoiceDefinition(this.currentResult.nodeId,[],this.currentDefinition,e)},applyDefaultProperties:function(e){return i.extend({},{selectorFormat:"combo"},e)},setFormat:function(e){this.updateTableStyle("selectorFormat",e)},setOrientation:function(e){this.updateTableStyle("selectorOrientation",e,!0),"v"==e?i(this.tagId).find(".selector").addClass("orientation-vertical"):i(this.tagId).find(".selector").removeClass("orientation-vertical")},updateTableStyle:function(e,t,n){var l=this.applyDefaultProperties(this.currentResult.itemProperties);l[e]=t,this.currentResult.itemProperties=l,n||i(this.tagId).trigger("evaluateNodeFromCurrentResult")},getOptionsMenu:function(){var e=this,t={callback:function(t){switch(t){case"_full":e.fullScreen();break;case"_knowledge":e.openDocumentationModal();break;case"_workflow":e.addTask();break;case"_view_in_diagram":e.viewInDiagram()}},items:{_full:{type:"icon_text",name:(0,r.translate)("fullscreen"),iconClass:"fa fa-expand"},sep2:"---------"}};return t.items._knowledge={type:"icon_text",name:(0,r.translate)("documentation"),iconClass:"fa fa-graduation-cap"},(0,r.haveAnyAccess)("LISTASSIGNEDWORKFLOWTASKS,LISTALLWORKFLOWTASKS")&&(t.items._workflow={type:"icon_text",name:(0,r.translate)("workflow"),iconClass:"fa fa-tasks"}),(0,r.haveAccess)("view_influence_diagram")&&(t.items._view_in_diagram={type:"icon_text",name:(0,r.translate)("view_in_diagram"),iconClass:"fa fa-sitemap"}),e.fromEmbedded&&(delete t.items._export,delete t.items.sep2,delete t.items._splitBy,delete t.items._knowledge,delete t.items._workflow,delete t.items._view_in_diagram),t},addTask:function(){var e=this;n.e(10).then(function(){var t=[n(703)];(function(t){(new t).showAddTaskForNode(e.currentNodeId)}).apply(null,t)}).catch(n.oe)}})}.apply(t,l))||(e.exports=a)}).call(this,n(1))}}]);
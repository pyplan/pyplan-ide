/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[237],{1974:function(t,e,n){"use strict";(function(a,i){var o,s,l=function(t){return t&&t.__esModule?t:{default:t}}(n(964));o=[n(1975)],void 0===(s=function(t){return a.View.extend({el:i("#main"),hotInstance:null,result:null,render:function(){var e=this,n=i("#wizardPandasIndex");n&&n.remove(),this.$el.append(t({title:this.options.title,max_height:"".concat(i(window).height()-200,"px")}));var a=i("#wizardPandasIndex"),o=a.find(".modal-footer .btnSave");a.on("hidden.bs.modal",function(){a.off("hidden.bs.modal"),a.remove()}).modal("show"),o.on("click",function(){a.modal("hide"),e.options.callback(e.result)}),this.instanceTableMode()},splitItems:function(t){var e,n,a=[],i="",o="";if(t.length>0){for(var s=0;s<t.length;s++)"'"!==(e=t.charAt(s))&&'"'!==e||(n?o===e&&(n=!1):(n=!0,o=e)),","!=e||n||(e="|-##SEP##-|",o=""),i+=e;a=i.split("|-##SEP##-|")}return a},resize:function(){},getDataForTable:function(){var t=this.options.definition;if(t&&t){var e=t.split(new RegExp("\\[(.*)\\]"))[1];return e||[]}return[]},updatePropertiesOnHandsonChange:function(t){var e=t.getData(),n=e.length-1;null!==e[n][0]&&""!==e[n][0]||e.splice(n,1),this.result="result = pd.Index(["+e+"])"},optimizeDataSource:function(t){for(var e,n,a=[],i=this.splitItems(t),o=0;o<i.length;o++)i[o]=i[o].trim(),n=new Object,e=(e=(1254316*Math.random()).toString()).substring(0,e.indexOf(".")),n.val=i[o],a.push(n);return a},instanceTableMode:function(){var t=this;this.hotInstance&&(this.hotInstance.destroy(),this.hotInstance=null);var e=this.$el.find(".tableDef"),n=this.getDataForTable(),a=n?this.optimizeDataSource(n):n;this.hotInstance=new l.default(e.get(0),{data:a,colWidths:[520],height:300,manualColumnResize:!0,rowHeaders:!0,colHeaders:["List"],minSpareRows:1,maxCols:1,readOnly:this.options.onBrowserMode,afterRemoveRow:function(e,n){t.updatePropertiesOnHandsonChange(this)},afterCreateRow:function(t,e){var n=this;setTimeout(function(){n.getDataAtCell(t,0)||n.countRows()-1===t||(n.selectCell(t,0),n.getActiveEditor().beginEditing())},200)},beforeChange:function(t,e){for(var n,a,o=0;o<t.length;o++){var s;if(!i.isNumeric(t[o][3]))n=(s=t[o][3]).charAt(0),a=s.charAt(s.length-1),'"'!==n&&'"'!==a&&"'"!==n&&"'"!==a&&(t[o][3]="'"+t[o][3]+"'")}},afterChange:function(e,n){if("loadData"!==n){for(var a=0;a<e.length;a++)""===e[a][3]&&this.alter("remove_row",e[a][0],1,!1);t.updatePropertiesOnHandsonChange(this)}}});var o=this.options.onBrowserMode;this.hotInstance.updateSettings({contextMenu:!o&&["row_above","row_below","remove_row"]},o)}})}.apply(e,o))||(t.exports=s)}).call(this,n(218),n(1))},1975:function(t,e,n){var a=n(690);t.exports=(a.default||a).template({compiler:[7,">= 4.0.0"],main:function(t,e,n,a,i){var o,s=null!=e?e:t.nullContext||{},l=n.helperMissing,r=t.escapeExpression;return"<div id='wizardPandasIndex' class='modal fade nodeWizardDialog' tabindex='-1' role='dialog' aria-labelledby='Wizard'\n  aria-hidden='true'>\n  <div class='modal-dialog'>\n    <div class='modal-content'>\n      <div class='modal-header'>\n        <button type='button' class='close' data-dismiss='modal' aria-hidden='true'>x</button>\n        <h4>"+r("function"==typeof(o=null!=(o=n.title||(null!=e?e.title:e))?o:l)?o.call(s,{name:"title",hash:{},data:i}):o)+"</h4>\n      </div>\n      <div class='modal-body' style=\"max-height:"+r("function"==typeof(o=null!=(o=n.max_height||(null!=e?e.max_height:e))?o:l)?o.call(s,{name:"max_height",hash:{},data:i}):o)+"\">\n        <div class='handsonWrapper tableDef' style='overflow: auto;'>\n        </div>\n      </div>\n      <div class='modal-footer'>\n        <button type='button' class='btn btn-default' data-dismiss='modal'>Cancel</button>\n        <button type='button' class='btn btn-primary btnSave'>Ok</button>\n      </div>\n    </div>\n  </div>\n</div>"},useData:!0})}}]);
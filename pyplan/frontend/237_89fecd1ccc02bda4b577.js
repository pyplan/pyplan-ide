/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[237],{1987:function(n,a,e){"use strict";(function(l,t){var s,i,o=function(n){return n&&n.__esModule?n:{default:n}}(e(884)),c=e(18);function r(n){return function(n){if(Array.isArray(n)){for(var a=0,e=new Array(n.length);a<n.length;a++)e[a]=n[a];return e}}(n)||function(n){if(Symbol.iterator in Object(n)||"[object Arguments]"===Object.prototype.toString.call(n))return Array.from(n)}(n)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance")}()}function d(n,a,e){return a in n?Object.defineProperty(n,a,{value:e,enumerable:!0,configurable:!0,writable:!0}):n[a]=e,n}s=[e(219),e(1988)],void 0===(i=function(n,a){return l.View.extend({el:t("#main"),currentFile:null,tableSchemaInstance:null,render:function(e){var l=this;this.$el.find("#main-modal").length>0||(new n).getFilesForImportWizard("csv",function(n){var s=a(function(n){for(var a=1;a<arguments.length;a++){var e=null!=arguments[a]?arguments[a]:{},l=Object.keys(e);"function"==typeof Object.getOwnPropertySymbols&&(l=l.concat(Object.getOwnPropertySymbols(e).filter(function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),l.forEach(function(a){d(n,a,e[a])})}return n}({},e,{files:n}));l.$el.append(s),t(".form-wizard").length>0&&(t(".form-wizard").formwizard({formPluginEnabled:!0,validationEnabled:!0,focusFirstInput:!1,disableUIStyles:!0,formOptions:{beforeSubmit:function(n){if(l.tableSchemaInstance){var a=l.tableSchemaInstance.getData(),e=[];t.each(a,function(n,a){a[2]&&e.push(a[0])}),l.refreshPreview(t(".selectEncoding").val(),t(".selectSeparator").val(),t(".selectRows").val(),e)}},dataType:"json",resetForm:!0}}),t(".form-wizard").bind("before_step_shown",function(n,a){a.isFirstStep?t(".wizardNext").hide():t(".wizardNext").show(),"thirdStep"===a.currentStep&&l.refreshPreview(t(".selectEncoding").val(),t(".selectSeparator").val(),t(".selectRows").val(),[],"getColumns")})),t(".csvModal").on("change",".selectEncoding, .selectSeparator, .selectRows",function(n){l.refreshPreview(t(".selectEncoding").val(),t(".selectSeparator").val(),t(".selectRows").val(),[],"readFile")}),t(".csvModal").on("click",".onReadUrl",function(n){l.currentFile=t("#main-modal").find(".txtUrl").val(),l.refreshPreview("auto","auto",200,[],"readFile"),t(".wizardNext").click()}),t(".csvModal").on("change",".selLocalFiles",function(n){l.currentFile=t("#main-modal").find(".selLocalFiles").val(),l.refreshPreview("auto","auto",200,[],"readFile"),t(".wizardNext").click()}),l.createUploader(),t("#modelInfoModal").length>0&&t("#modelInfoModal").modal("hide"),e.hasOwnProperty("html")&&t("#main-modal .modal-body").html(e.html),t("#main-modal .modal-footer button").click(function(){var n=!0;return e.callback&&!1===e.callback.call(this,t(this).attr("data-code"),t("#main-modal"))&&(n=!1),n&&(t("#main-modal").off("shown"),t("#main-modal").modal("hide")),!1}),t("#main-modal").on("show.bs.modal",function(){if(0===t("#main-modal:visible").length){var n=1040+10*t(".modal:visible").length;t(this).css("z-index",n),setTimeout(function(){t(".modal-backdrop").not(".modal-stack").css("z-index",n-10).addClass("modal-stack")},0),e.hasOwnProperty("onLoad")&&e.onLoad(t("#main-modal")),!0!==e.okOnEnter&&void 0!==e.okOnEnter||t("#main-modal").keyup(function(n){13==n.keyCode&&t("#main-modal button.btn-primary").click()})}}),t("#main-modal").on("hidden.bs.modal",function(){t("#main-modal").off("hidden"),e.hasOwnProperty("onClose")&&e.onClose(t("#main-modal")),t("#main-modal").remove()});var i=null;e.backdrop&&(i={backdrop:"static",keyboard:!1}),t("#main-modal").modal(i)})},createUploader:function(){var n=this,a=t("#plupload");t("#plupload").css("position","relative"),t("#plupload").css("z-index","1000"),t("#plupload").css("width","100%"),t("#plupload").css("height","300px"),a.pluploadQueue({runtimes:"html5",url:"".concat(__apiURL,"/fileManager/upload/"),headers:{Authorization:"Token ".concat(__currentToken),"session-key":__currentSession.session_key},file_data_name:"files",max_file_size:"0",chunk_size:"10mb",unique_names:!1,filters:{title:"Text and CSV",extensions:"txt,csv,gzip,zip"},flash_swf_url:"js/plupload/plupload.flash.swf",silverlight_xap_url:"js/plupload/plupload.silverlight.xap",multipart_params:{action:"uploadFileToModelFolder",folder_path:__currentSession.modelInfo.uri.substring(0,__currentSession.modelInfo.uri.lastIndexOf("/"))},init:{FilesAdded:function(n,a){t(".fileError").hide(),n.start(),t("#plupload_browse").prop("disabled",!0),t("#plupload_browse").hide(),t("#uploading").show()},UploadComplete:function(a,e){n.currentFile=e[0].name,n.refreshPreview("auto","auto",200,[],"readFile"),t(".wizardNext").click(),a.splice(),a.refresh(),t("#plupload_browse").prop("disabled",!1),t("#plupload_browse").show(),t("#uploading").hide()},FileUploaded:function(n,a,e){},Error:function(n,a){(0,c.showMessage)(a.code+": "+a.message,null,"error")}}}),t(".plupload_filelist_footer").css("height","auto"),t(".plupload_header").remove(),t(".plupload_progress_container").addClass("progress").addClass("progress-striped"),t(".plupload_progress_bar").addClass("bar"),t(".plupload_button").each(function(){t(this).hasClass("plupload_add")?(t(this).attr("class","btn plupload_add btn-primary").html("<i class='fa fa-plus-circle'></i> "+t(this).html()),t(this).addClass("btn-small")):(t(this).attr("class","btn plupload_start btn-success").html("<i class='fa fa-cloud-upload'></i> "+t(this).html()),t(this).hide())}),t("#plupload_filelist").bind("drop",function(n){var e=(a=t("#plupload")).pluploadQueue();e.splice(),e.refresh()}).bind("dragleave",function(n){return!1})},refreshPreview:function(n,a,l,s,i){var o=this,c={wizard:"sourcecsv",action:i,params:{filename:o.currentFile,encoding:n,sep:a,rows:l}};"Submit"===t(".wizardNext").val()&&(c.action="generateDefinition",c.params.nodeId=o.options.nodeData.identifier),s.length>0&&(c.params.indexes=s),Promise.resolve().then(function(){var n=[e(219)];(function(n){(new n).callWizard(c,function(n){"ok"===n?(t("#main-modal").modal("hide"),e.e(20).then(function(){var n=[e(739)];(function(n){o.options.nodeData.id||(o.options.nodeData.id=o.options.nodeData.identifier),(new n).loadDefinitionTab(o.options.nodeData,!1,".btnTabWizard")}).apply(null,n)}).catch(e.oe)):"getColumns"===i?o.initSchemaGrid(n):o.initGrid(n.result)},function(n){})}).apply(null,n)}).catch(e.oe)},initGrid:function(n){for(var a=n.schema.fields,e={columns:[],data:n.data,colHeaders:[],height:450,stretchH:"all",readOnly:!0},l=0;l<a.length;l++){var s={};s.data=a[l].name,e.colHeaders.push(a[l].name),e.columns.push(s)}var i=t(".handsonGrid").get(0);setTimeout(function(){new o.default(i,e)},500)},initSchemaGrid:function(n){var a=this,e=t(".btnSelectAll"),l=t(".btnUnselectAll"),s={columns:[{data:"field",readOnly:!0},{data:"dtype",readOnly:!0},{data:"isIndex",type:"checkbox"}],data:n.map(function(n){return n.isIndex="index"===n.type,n}),colHeaders:["Field","Type","Is index"],colWidths:[null,15,10],height:450,stretchH:"all",manualColumnResize:!0,manualRowResize:!0,afterRenderer:function(n,a,e){2===e&&t(n).css("text-align","center")}},i=t(".handsonSchema").get(0);setTimeout(function(){a.tableSchemaInstance=new o.default(i,s),e.on("click",function(n){n.preventDefault(),n.stopPropagation();var e=a.tableSchemaInstance.countRows();r(Array(e)).forEach(function(n,e){a.tableSchemaInstance.setDataAtCell(e,2,!0)})}),l.on("click",function(n){n.preventDefault(),n.stopPropagation();var e=a.tableSchemaInstance.countRows();r(Array(e)).forEach(function(n,e){a.tableSchemaInstance.setDataAtCell(e,2,!1)})})},500)}})}.apply(a,s))||(n.exports=i)}).call(this,e(218),e(1))},1988:function(n,a,e){var l=e(690);n.exports=(l.default||l).template({1:function(n,a,e,l,t){var s,i,o=n.escapeExpression;return'                        <option value="'+o(n.lambda(null!=(s=null!=a?a.data:a)?s.fullPath:s,a))+'">'+o("function"==typeof(i=null!=(i=e.text||(null!=a?a.text:a))?i:n.hooks.helperMissing)?i.call(null!=a?a:n.nullContext||{},{name:"text",hash:{},data:t,loc:{start:{line:69,column:58},end:{line:69,column:66}}}):i)+"</option>\n"},3:function(n,a,e,l,t){var s,i=null!=a?a:n.nullContext||{},o=n.hooks.helperMissing,c=n.escapeExpression;return'        <button class="btn btn-'+c("function"==typeof(s=null!=(s=e.css||(null!=a?a.css:a))?s:o)?s.call(i,{name:"css",hash:{},data:t,loc:{start:{line:261,column:31},end:{line:261,column:38}}}):s)+'" data-code="'+c("function"==typeof(s=null!=(s=e.code||(null!=a?a.code:a))?s:o)?s.call(i,{name:"code",hash:{},data:t,loc:{start:{line:261,column:51},end:{line:261,column:59}}}):s)+'" data-dismiss="modal" aria-hidden="true">'+c("function"==typeof(s=null!=(s=e.title||(null!=a?a.title:a))?s:o)?s.call(i,{name:"title",hash:{},data:t,loc:{start:{line:261,column:101},end:{line:261,column:110}}}):s)+"</button>\n"},compiler:[8,">= 4.3.0"],main:function(n,a,e,l,t){var s,i,o=null!=a?a:n.nullContext||{};return'<div id="main-modal" class="modal fade csvModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"\n  aria-hidden="true" style="display: none;">\n  <div class="modal-dialog '+n.escapeExpression("function"==typeof(i=null!=(i=e.modalClass||(null!=a?a.modalClass:a))?i:n.hooks.helperMissing)?i.call(o,{name:"modalClass",hash:{},data:t,loc:{start:{line:3,column:27},end:{line:3,column:41}}}):i)+'">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">x</button>\n        <h4 class="modal-title" id="myModalLabel">CSV Data source</h4>\n      </div>\n\n      <div class="modal-body" style="overflow-y:auto; overflow-x: hidden;">\n        <div class="box-content">\n          <form class="form-horizontal form-wizard ui-formwizard" id="csvForm" novalidate="novalidate">\n            <div class="step ui-formwizard-content" id="firstStep" style="display: block;">\n              <ul class="wizard-steps steps-3">\n                <li class="active">\n                  <div class="single-step">\n                    <span class="title">\n                      1</span>\n                    <span class="circle">\n                      <span class="active"></span>\n                    </span>\n                    <span class="description">\n                      Read CSV file\n                    </span>\n                  </div>\n                </li>\n                <li>\n                  <div class="single-step">\n                    <span class="title">\n                      2</span>\n                    <span class="circle">\n                    </span>\n                    <span class="description">\n                      Data Preview\n                    </span>\n                  </div>\n                </li>\n                <li>\n                  <div class="single-step">\n                    <span class="title">\n                      3</span>\n                    <span class="circle">\n                    </span>\n                    <span class="description">\n                      Schema\n                    </span>\n                  </div>\n                </li>\n              </ul>\n              <div class="step-forms">\n                <div class="fileError" style="display: none;">ERROR FILE FORMAT</div>\n\n                <div id="plupload">\n                </div>\n\n                <span class="lblSeparator">OR</span>\n                <div class="separator"></div>\n                <div style="clear:both;"></div>\n\n                <div class="row">\n                  <div class="form-group">\n                    <label for="textfield" class="control-label col-sm-3" style="text-align:left;">\n                      From server:\n                    </label>\n                    <div class="col-sm-9">\n                      <select name="select" class="form-control selLocalFiles">\n                        <option value=""> Select a file </option>\n'+(null!=(s=e.each.call(o,null!=a?a.files:a,{name:"each",hash:{},fn:n.program(1,t,0),inverse:n.noop,data:t,loc:{start:{line:68,column:24},end:{line:70,column:33}}}))?s:"")+'\n                      </select>\n                    </div>\n                  </div>\n                </div>\n\n                <span class="lblSeparator">OR</span>\n                <div class="separator"></div>\n                <div style="clear:both;"></div>\n\n                <div class="row">\n                  <div class="form-group">\n                    <label for="textfield" class="control-label col-sm-3" style="text-align:left;">\n                      From URL:\n                    </label>\n                    <div class="col-sm-9">\n                      <div class="input-group">\n                        <input type="text" placeholder="http://yoururl/file.csv" class="form-control txtUrl">\n                        <div class="input-group-btn">\n                          <button class="btn btn-primary onReadUrl" type="button">Read</button>\n                        </div>\n                      </div>\n                    </div>\n                  </div>\n                </div>\n\n              </div>\n            </div>\n            <div class="step ui-formwizard-content" id="secondStep" style="display: none;">\n              <ul class="wizard-steps steps-3">\n                <li>\n                  <div class="single-step">\n                    <span class="title">\n                      1</span>\n                    <span class="circle">\n\n                    </span>\n                    <span class="description">\n                      Read CSV file\n                    </span>\n                  </div>\n                </li>\n                <li class="active">\n                  <div class="single-step">\n                    <span class="title">\n                      2</span>\n                    <span class="circle">\n                      <span class="active"></span>\n                    </span>\n                    <span class="description">\n                      Data Preview\n                    </span>\n                  </div>\n                </li>\n                <li>\n                  <div class="single-step">\n                    <span class="title">\n                      3</span>\n                    <span class="circle">\n                    </span>\n                    <span class="description">\n                      Schema\n                    </span>\n                  </div>\n                </li>\n              </ul>\n              <div class="form-group">\n\n                <div class="row">\n                  <div class="col-sm-4">\n                    <div class="form-group">\n                      <label for="textfield" class="control-label">Encoding</label>\n                      <select name="select" class="form-control selectEncoding">\n                        <option value="auto">Auto</option>\n                        <option value="ascii">us-ascii</option>\n                        <option value="cp850">IBM850</option>\n                        <option value="cp852">IBM852</option>\n                        <option value="cp1251">windows-1251</option>\n                        <option value="cp1252">windows-1252</option>\n                        <option value="utf_8">UTF-8</option>\n                        <option value="utf_16">UTF-16</option>\n                        <option value="latin_1">latin1</option>\n                      </select>\n                    </div>\n                  </div>\n                  <div class="col-sm-4">\n                    <div class="form-group">\n                      <label for="textfield" class="control-label">Separator</label>\n                      <select name="select" class="form-control selectSeparator">\n                        <option value="auto">Auto</option>\n                        <option value=","> , </option>\n                        <option value=";"> ; </option>\n                        <option value="\t">Tab</option>\n                        <option value=" ">Space</option>\n                        <option value="|"> | </option>\n                      </select>\n                    </div>\n                  </div>\n                  <div class="col-sm-4">\n                    <div class="form-group">\n                      <label for="textfield" class="control-label">Rows</label>\n                      <select name="select" class="form-control selectRows">\n                        <option value="10">10</option>\n                        <option value="50">50</option>\n                        <option value="100">100</option>\n                        <option value="200" selected>200</option>\n                        <option value="500">500</option>\n                        <option value="1000">1000</option>\n                      </select>\n                    </div>\n                  </div>\n                </div>\n\n                <div class="row">\n                  <div class="col-sm-12">\n                    <div class="handsonGrid" style="width:100%; height:100%;"></div>\n                  </div>\n                </div>\n\n              </div>\n\n            </div>\n            <div class="step ui-formwizard-content" id="thirdStep" style="display: none;">\n              <ul class="wizard-steps steps-3">\n                <li>\n                  <div class="single-step">\n                    <span class="title">\n                      1</span>\n                    <span class="circle">\n\n                    </span>\n                    <span class="description">\n                      Read CSV file\n                    </span>\n                  </div>\n                </li>\n                <li>\n                  <div class="single-step">\n                    <span class="title">\n                      2</span>\n                    <span class="circle">\n\n                    </span>\n                    <span class="description">\n                      Data Preview\n                    </span>\n                  </div>\n                </li>\n                <li class="active">\n                  <div class="single-step">\n                    <span class="title">\n                      3</span>\n                    <span class="circle">\n                      <span class="active"></span>\n                    </span>\n                    <span class="description">\n                      Schema\n                    </span>\n                  </div>\n                </li>\n              </ul>\n              <div class="form-group">\n                <div class="row">\n                  <div class="col-sm-12">\n                    <div class="handsonActions text-right">\n                      <button type=\'button\' class=\'btn btn-green btnSelectAll\' rel=\'tooltip\'\n                        data-original-title=\'Select All\'>\n                        <i class=\'fa fa-check\' />Select All\n                      </button>\n                      <button type=\'button\' class=\'btn btn-orange btnUnselectAll\' rel=\'tooltip\'\n                        data-original-title=\'Unselect All\'>\n                        <i class="fa fa-times" /> Unselect All\n                      </button>\n                    </div>\n                    <div class="handsonSchema" style="width:100%; height:100%;"></div>\n                  </div>\n                </div>\n              </div>\n            </div>\n\n            <div class="form-actions">\n              <input type="reset" class="btn ui-wizard-content ui-formwizard-button" value="Back" id="back">\n              <input type="submit" class="btn btn-primary ui-wizard-content ui-formwizard-button wizardNext nodisplay"\n                value="Next" id="next">\n            </div>\n          </form>\n        </div>\n      </div>\n      <div class="modal-footer">\n'+(null!=(s=e.each.call(o,null!=a?a.buttons:a,{name:"each",hash:{},fn:n.program(3,t,0),inverse:n.noop,data:t,loc:{start:{line:260,column:8},end:{line:262,column:17}}}))?s:"")+"      </div>\n    </div>\n  </div>\n</div>"},useData:!0})}}]);
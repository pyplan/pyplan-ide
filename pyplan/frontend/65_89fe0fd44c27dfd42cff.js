/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[65,27,284],{1296:function(e,n,t){var a=t(670);function l(e){return e&&(e.__esModule?e.default:e)}e.exports=(a.default||a).template({1:function(e,n,a,s,o,i,c){var r,d=e.lambda,p=e.escapeExpression,u=null!=n?n:e.nullContext||{},m=e.lookupProperty||function(e,n){if(Object.prototype.hasOwnProperty.call(e,n))return e[n]};return'  <div class="form-group" param-name="'+p(d(null!=n?m(n,"name"):n,n))+'">\n    <label for="textfield" class="control-label col-xs-4 col-sm-4 col-md-3">'+p(d(null!=n?m(n,"label"):n,n))+'</label>\n    <div class="col-xs-8 col-sm-8 col-md-9">\n'+(null!=(r=l(t(669)).call(u,null!=n?m(n,"paramType"):n,"==","select",{name:"ifCond",hash:{},fn:e.program(2,o,0,i,c),inverse:e.noop,data:o,loc:{start:{line:7,column:6},end:{line:13,column:17}}}))?r:"")+"\n"+(null!=(r=l(t(669)).call(u,null!=n?m(n,"paramType"):n,"==","checkbox",{name:"ifCond",hash:{},fn:e.program(6,o,0,i,c),inverse:e.noop,data:o,loc:{start:{line:15,column:6},end:{line:17,column:17}}}))?r:"")+"\n"+(null!=(r=l(t(669)).call(u,null!=n?m(n,"paramType"):n,"==","input",{name:"ifCond",hash:{},fn:e.program(8,o,0,i,c),inverse:e.noop,data:o,loc:{start:{line:19,column:6},end:{line:21,column:17}}}))?r:"")+"    </div>\n  </div>\n"},2:function(e,n,t,a,l,s,o){var i,c=e.lookupProperty||function(e,n){if(Object.prototype.hasOwnProperty.call(e,n))return e[n]};return'      <select name="paramType" class="select2-me paramType" style="width:250;">\n'+(null!=(i=c(t,"each").call(null!=n?n:e.nullContext||{},null!=n?c(n,"list"):n,{name:"each",hash:{},fn:e.program(3,l,0,s,o),inverse:e.noop,data:l,loc:{start:{line:9,column:8},end:{line:11,column:17}}}))?i:"")+"      </select>\n"},3:function(e,n,a,s,o,i,c){var r,d=e.lambda,p=e.escapeExpression,u=e.lookupProperty||function(e,n){if(Object.prototype.hasOwnProperty.call(e,n))return e[n]};return'        <option value="'+p(d(n,n))+'" '+(null!=(r=l(t(669)).call(null!=n?n:e.nullContext||{},null!=c[1]?u(c[1],"defaultValue"):c[1],"==",n,{name:"ifCond",hash:{},fn:e.program(4,o,0,i,c),inverse:e.noop,data:o,loc:{start:{line:10,column:33},end:{line:10,column:102}}}))?r:"")+">"+p(d(n,n))+"</option>\n"},4:function(e,n,t,a,l){return' selected="selected" '},6:function(e,n,t,a,l){var s=e.lookupProperty||function(e,n){if(Object.prototype.hasOwnProperty.call(e,n))return e[n]};return'      <input type="checkbox" class="paramType" checked="'+e.escapeExpression(e.lambda(null!=n?s(n,"defaultValue"):n,n))+'">\n'},8:function(e,n,t,a,l){var s=e.lookupProperty||function(e,n){if(Object.prototype.hasOwnProperty.call(e,n))return e[n]};return'      <input type="text" class="form-control" value="'+e.escapeExpression(e.lambda(null!=n?s(n,"defaultValue"):n,n))+'">\n'},compiler:[8,">= 4.3.0"],main:function(e,n,t,a,l,s,o){var i,c=e.lookupProperty||function(e,n){if(Object.prototype.hasOwnProperty.call(e,n))return e[n]};return'<form class="form-horizontal form-bordered">\n\n'+(null!=(i=c(t,"each").call(null!=n?n:e.nullContext||{},null!=n?c(n,"params"):n,{name:"each",hash:{},fn:e.program(1,l,0,s,o),inverse:e.noop,data:l,loc:{start:{line:3,column:2},end:{line:24,column:11}}}))?i:"")+"</form>"},useData:!0,useDepths:!0})},1642:function(e,n,t){"use strict";(function(a,l){var s,o,i,c=t(18),r=(i=t(223))&&i.__esModule?i:{default:i};s=[t(664),t(748),t(739),t(713),t(2621),t(1296)],void 0===(o=function(e,n,s,o,i,d){return a.View.extend({el:l("#main"),taskSchedulerCtrl:new n,initialize:function(){},render:function(e){l('.container-fluid.mainTask[data-rel="etl-task"]').remove();var n=this,a=__currentSession.companyId;(new o).List(a,(function(a){if(n.options.tasksList)for(var s=0;s<n.options.tasksList.length;s++)n.options.tasksList[s].id=n.options.tasksList[s].scheduleTaskId,n.options.tasksList[s].text=n.options.tasksList[s].scheduleTaskName;else n.options.tasksList=[];var o={users:a,tasks:n.options.tasksList},c=i(o);n.$el.append(c),n.instanceTable(),l(".relatedComplete").select2({data:n.options.tasksList}).on("change",(function(){n.$el.find(".relatedCompleteParams").empty();var e=l(this).select2("data"),t=d(e);n.$el.find(".relatedCompleteParams").append(t)})),l(".relatedFail").select2({data:n.options.tasksList}).on("change",(function(){n.$el.find(".relatedFailParams").empty();var e=l(this).select2("data"),t=d(e);n.$el.find(".relatedFailParams").append(t)}));var p="New ETL task";e&&(p="Edit ETL task",n.fillForm(e)),Promise.resolve().then((function(){var e=[t(664)];(function(e){(new e).hideAllTasks(),(new e).addSimpleTask("etl-task",p),(new e).selectTask("etl-task",p)}).apply(null,e)})).catch(t.oe);var u=l(".etl-task-content");function m(){var e=l(window).height();e-=95,u.height(e-(l(".page-header").height()+20))}l(window).resize(m),m(),l(".tagsinput").length>0&&l(".tagsinput").each((function(e){l(n).tagsInput({width:"auto",height:"auto"})})),l(".instances").TouchSpin({min:0,max:50,step:1,decimals:0,boostat:5,maxboostedstep:10,forcestepdivisibility:"none"}),l(".datepick").length>0&&l(".datepick").each((function(){var n=l(this);n.datepicker(),e||n.datepicker("setValue",(0,r.default)().format("YYYY/MM/DD")),n.on("changeDate",(function(){n.datepicker("hide")}))})),l(".timepick").length>0&&l(".timepick").timepicker({defaultTime:"current",minuteStep:1,disableFocus:!0,template:"dropdown"}),l(".chosen-select").chosen({disable_search_threshold:10}),l(".task-log-btn").on("click",(function(){return n.showTaskLog(event,n),!1})),l(".select-trigger").on("change",(function(e){return n.triggerChange(e.currentTarget.value,n),!1})),l(".save").on("click",(function(){return n.save(n,e),!1})),l(".cancel").on("click",(function(){return n.cancel(n),!1})),n.$el.find(".add-param").on("click",(function(e){return n.openParamModal(null,n,e),!1})),l("div[data-rel='etl-task']").find("div.abm-top-options a.btn-close").on("click",n.close);var h=l("#right-column").height();l("#tree-container").height(h),n.getThis().on("removeView",(function(){n.onRemoveView()})),n.getThis().on("beforeRemoveView",(function(e,t){n.onBeforeRemoveView(e,t)}))}))},close:function(){Promise.resolve().then((function(){var e=[t(664)];(function(e){(new e).removeTask("etl-task")}).apply(null,e)})).catch(t.oe)},cancel:function(e){e.taskSchedulerCtrl.listTasks("etl-tasks"),e.close()},fillForm:function(e){var n=l(".run-model-days input[type=checkbox]");if(e.days){var t=e.days.split(",");l(t).each((function(e,t){n.each((function(e,n){l(n).val()===t.toString()&&l(n).attr("checked","checked")}))}))}l("#selTrigger option").each((function(n,t){l(t).val()===e.scheduleRunType.toString()&&l(t).attr("selected",!0)})),this.triggerChange(e.scheduleRunType.toString(),this),l("#selStatesToLog option").each((function(n,t){l(t).val()===e.scheduleLogType.toString()&&l(t).attr("selected",!0)})),l("#chkEnabled").prop("checked",e.enabled);var a,s=e.nextRunDate.split("T");if(l("#txtDate").val(s[0]),l("#txtTime").val(s[1]),l("#txtTaskName").val(e.scheduleTaskName),l("#txtFile").val(e.filePath),l(".selOnStart").val(null!==e.onStart?e.onStart.split(","):""),l(".selOnComplete").val(null!==e.onComplete?e.onComplete.split(","):""),l(".selOnFail").val(null!==e.onFail?e.onFail.split(","):""),null!==e.params&&e.params.length>0)for(var o=0;o<e.params.length;o++)this.$el.find(".paramList").DataTable().row.add(e.params[o]).draw();if(null!==e.relatedOnComplete){l(".chkEnabledComplete").attr("checked",e.relatedOnComplete.enabled),l(".relatedComplete").select2("val",e.relatedOnComplete.scheduleTaskId),l(".relatedComplete").trigger("change");var i=l(".relatedCompleteParams").find("div.form-group");l.each(i,(function(n,t){l(this).find("select").length>0?l(this).find("select").val(e.relatedOnComplete.params[n].value):l(this).find('input[type="text"]').length>0?l(this).find('input[type="text"]').val(e.relatedOnComplete.params[n].value):(a="true"===e.relatedOnComplete.params[n].value,l(this).find('input[type="checkbox"]').attr("checked",a))}))}if(null!==e.relatedOnFail){l(".chkEnabledFail").attr("checked",e.relatedOnFail.enabled),l(".relatedFail").select2("val",e.relatedOnFail.scheduleTaskId),l(".relatedFail").trigger("change");i=l(".relatedFailParams").find("div.form-group");l.each(i,(function(n,t){l(this).find("select").length>0?l(this).find("select").val(e.relatedOnFail.params[n].value):l(this).find('input[type="text"]').length>0?l(this).find('input[type="text"]').val(e.relatedOnFail.params[n].value):(a="true"===e.relatedOnFail.params[n].value,l(this).find('input[type="checkbox"]').attr("checked",a))}))}},triggerChange:function(e,n){"0"===e?(l(".date-time").hide(),l(".run-model-days").hide(),l(".form-group.enabledCheckbox").show()):"1"===e?(l(".date-time").show(),l(".run-model-days").hide(),l("#lblDate").html("Date time"),l(".form-group.enabledCheckbox").show()):"2"===e?(l(".date-time").show(),l(".run-model-days").hide(),l("#lblDate").html("Start date"),l(".form-group.enabledCheckbox").show()):"3"===e?(l(".date-time").show(),l(".run-model-days").show(),l("#lblDate").html("Start date"),l(".form-group.enabledCheckbox").show()):"5"===e?(l(".date-time").show(),l(".run-model-days").hide(),l("#lblDate").html("Start date"),l(".form-group.enabledCheckbox").show()):(l(".date-time").hide(),l(".run-model-days").hide(),l(".form-group.enabledCheckbox").hide())},save:function(n,t){var a=l("#selTrigger").val(),o=l("#txtDate").val()+" "+l("#txtTime").val(),i=l("#selStatesToLog").val(),c=l("#chkEnabled").prop("checked"),r=null!==l(".selOnStart").chosen().val()?l(".selOnStart").chosen().val().toString():"",d=null!==l(".selOnComplete").chosen().val()?l(".selOnComplete").chosen().val().toString():"",p=null!==l(".selOnFail").chosen().val()?l(".selOnFail").chosen().val().toString():"",u=this.getRelatedOnParams("complete"),m=this.getRelatedOnParams("fail");4===a&&(c=!0);var h,f={scheduleTaskName:l("#txtTaskName").val(),scheduleRunType:a,scheduleLogType:i,enabled:c,filePath:l("#txtFile").val(),onStart:r,onComplete:d,onFail:p,relatedOnComplete:u,relatedOnFail:m};if("0"!==l(".select-trigger").val()&&(f.nextRunDate=o),"3"===l(".select-trigger").val()){for(var v="",b=l(".run-model-days input[type=checkbox]:checked"),y=0;y<b.length;y++)v=0===y?l(b[y]).val():v+","+l(b[y]).val();f.days=v}f.params=[];for(y=0;y<this.$el.find(".paramList").DataTable().data().length;y++)delete(h=this.$el.find(".paramList").DataTable().row(y).data()).indexTable,f.params.push(h);t?(f.scheduleTaskId=t.scheduleTaskId,(new s).updateETLTask(f,(function(t){(new e).removeTask("etl-task"),n.taskSchedulerCtrl.listTasks("etl-tasks")}))):(new s).createETLTask(f,(function(t){(new e).removeTask("etl-task"),n.taskSchedulerCtrl.listTasks("etl-tasks")}));return!1},getRelatedOnParams:function(e){var n,t,a;"complete"===e?(t="relatedComplete",n="relatedCompleteParams",a="chkEnabledComplete"):(t="relatedFail",n="relatedFailParams",a="chkEnabledFail");var s,o={scheduleTaskId:l("."+t).select2("val"),enabled:l("."+a).is(":checked"),params:[]},i=this.$el.find("."+n+" div.form-group");return l.each(i,(function(){s={name:l(this).attr("param-name")},l(this).find("select").length>0?(s.value=l(this).find("select").val(),s.paramType="select"):l(this).find('input[type="text"]').length>0?(s.value=l(this).find('input[type="text"]').val(),s.paramType="input"):(s.value=l(this).find('input[type="checkbox"]').is(":checked"),s.paramType="checkbox"),o.params.push(s)})),o},onAddParam:function(e,n){var t=n;null!==e.indexTable?t.$el.find(".paramList").DataTable().row(e.indexTable).data(e).draw():t.$el.find(".paramList").DataTable().row.add(e).draw()},openParamModal:function(e,n,a){n=n;return t.e(74).then((function(){var a=[t(1651)];(function(t){(new t).render(e,n,n.onAddParam)}).apply(null,a)})).catch(t.oe),a.preventDefault(),!1},instanceTable:function(){var e,n=this.$el.find(".paramList"),t=this,a=n.DataTable();a.clear(),a.destroy(),e=n.DataTable({searching:!1,paging:!1,ordering:!1,info:!1,columns:[{data:"paramType"},{data:"name"},{data:"label"},{data:"defaultValue"},{data:null}],columnDefs:[{width:"15%",targets:-1,defaultContent:'<button class="btn btn-small btn-primary edit-param" rel="tooltip" title="" data-original-title="'+(0,c.translate)("_edit_param")+'"> <i class="fa fa-pencil"></i></button><button class="btn btn-small btn-red remove-param" rel="tooltip" title="" data-original-title="'+(0,c.translate)("_delete_param")+'"> <i class="fa fa-trash"></i></button>'}]}),t.$el.find(".paramList tbody").on("click","button.edit-param",(function(n){var a=e.row(l(this).parents("tr")).data();a.indexTable=e.row(l(this).parents("tr")).index(),t.openParamModal(a,t,n),n.preventDefault()})),t.$el.find(".paramList tbody").on("click","button.remove-param",(function(n){var t=e.row(l(this).parents("tr")).index();e.row(t).remove().draw(),n.preventDefault()}))},getThis:function(){return this.$el.find(".mainTask[data-rel='knowledge-base']")},onRemoveView:function(){this.el=l("#main")},onBeforeRemoveView:function(e,n){this.$el.find(".mainTask[data-rel='knowledge-base']").remove()}})}.apply(n,s))||(e.exports=o)}).call(this,t(219),t(1))},2621:function(e,n,t){var a=t(670);function l(e){return e&&(e.__esModule?e.default:e)}e.exports=(a.default||a).template({1:function(e,n,t,a,l){var s=e.lambda,o=e.escapeExpression,i=e.lookupProperty||function(e,n){if(Object.prototype.hasOwnProperty.call(e,n))return e[n]};return'                    <option value="'+o(s(null!=n?i(n,"userId"):n,n))+'">'+o(s(null!=n?i(n,"userLogin"):n,n))+"</option>\n"},compiler:[8,">= 4.3.0"],main:function(e,n,a,s,o){var i,c=null!=n?n:e.nullContext||{},r=e.escapeExpression,d=e.lookupProperty||function(e,n){if(Object.prototype.hasOwnProperty.call(e,n))return e[n]};return'<div class="abm-base-tmp container-fluid mainTask" data-rel="etl-task" data-type="tab-content">\n\n  \x3c!-- LIST VIEW --\x3e\n\n  <div class="box etl-task-content">\n    <div class="box-title">\n      <h3><i class="fa fa-th-list"></i>Schedule ETL task</h3>\n      <div class="actions abm-top-options">\n        <a href="#" class="btn btn-close"><i class="fa fa-times"></i></a>\n      </div>\n    </div>\n    <div class="box-content abm-content">\n\n\n      <ul class="tabs tabs-inline tabs-top" style="border-color: #DDD; border-width: 0 0 1px 0; border-style: solid;">\n        <li class="active">\n          <a href="#etl-1" data-toggle="tab">\n            <i class="fa fa-cog"></i>General</a>\n        </li>\n        <li>\n          <a href="#etl-2" data-toggle="tab">\n            <i class="fa fa-clock"></i>Schedule</a>\n        </li>\n        <li>\n          <a href="#etl-3" data-toggle="tab">\n            <i class="fa fa-list-alt"></i>Params</a>\n        </li>\n        <li>\n          <a href="#etl-4" data-toggle="tab">\n            <i class="fa fa-chain"></i>Related tasks</a>\n        </li>\n      </ul>\n\n      <div class="form-horizontal form-bordered">\n        <div class="tab-content padding tab-content-inline tab-content-bottom">\n\n          \x3c!-- START TAB 1 --\x3e\n          <div class="tab-pane active" id="etl-1">\n            <div class="row">\n              <div class="form-group">\n                <label for="textfield" class="control-label col-sm-2">Task name</label>\n                <div class="col-sm-10">\n                  <input type="text" name="txtTaskName" id="txtTaskName" class="form-control">\n                </div>\n              </div>\n\n              <div class="form-group">\n                <label for="textfield" class="control-label col-sm-2">File</label>\n                <div class="col-sm-10">\n                  <input type="text" name="txtFile" id="txtFile" class="form-control">\n                </div>\n              </div>\n            </div>\n\n            <div class="row">\n              <div class="col-sm-12">\n                <h5>Send e-mail to:</h5>\n              </div>\n            </div>\n\n            <div class="row">\n              <div class="form-group">\n                <label for="textfield" class="control-label col-sm-2">On start</label>\n                <div class="col-sm-10">\n                  <select data-placeholder="Choose users.." style="width:450px;" multiple\n                    class="chosen-select selOnStart">\n'+(null!=(i=d(a,"each").call(c,null!=n?d(n,"users"):n,{name:"each",hash:{},fn:e.program(1,o,0),inverse:e.noop,data:o,loc:{start:{line:67,column:20},end:{line:69,column:29}}}))?i:"")+'                  </select>\n                </div>\n              </div>\n\n              <div class="form-group">\n                <label for="textfield" class="control-label col-sm-2">On complete</label>\n                <div class="col-sm-10">\n                  <select data-placeholder="Choose users.." style="width:450px;" multiple\n                    class="chosen-select selOnComplete">\n'+(null!=(i=d(a,"each").call(c,null!=n?d(n,"users"):n,{name:"each",hash:{},fn:e.program(1,o,0),inverse:e.noop,data:o,loc:{start:{line:79,column:20},end:{line:81,column:29}}}))?i:"")+'                  </select>\n                </div>\n              </div>\n\n              <div class="form-group">\n                <label for="textfield" class="control-label col-sm-2">On fail</label>\n                <div class="col-sm-10">\n                  <select data-placeholder="Choose users.." style="width:450px;" multiple\n                    class="chosen-select selOnFail">\n'+(null!=(i=d(a,"each").call(c,null!=n?d(n,"users"):n,{name:"each",hash:{},fn:e.program(1,o,0),inverse:e.noop,data:o,loc:{start:{line:91,column:20},end:{line:93,column:29}}}))?i:"")+'                  </select>\n                </div>\n              </div>\n\n            </div>\n          </div>\n          \x3c!-- END TAB 1 --\x3e\n\n\n          \x3c!-- START TAB 2 --\x3e\n          <div class="tab-pane" id="etl-2">\n            <div class="row">\n              <div class="col-sm-6">\n\n                <div class="form-group">\n                  <label for="textfield" class="control-label col-sm-4">Trigger</label>\n                  <div class="col-sm-8">\n                    <select name="selTrigger" id="selTrigger" class="form-control select-trigger">\n                      <option value="0">Always</option>\n                      <option value="1">One time</option>\n                      <option value="2">Daily</option>\n                      <option value="3">Weekly</option>\n                      <option value="5">Monthly</option>\n                      <option value="4">Manual</option>\n                    </select>\n                  </div>\n                </div>\n\n                <div class="form-group">\n                  <label for="textfield" class="control-label col-sm-4">States to log</label>\n                  <div class="col-sm-8">\n                    <select name="selStatesToLog" id="selStatesToLog" class="form-control">\n                      <option value="0">All</option>\n                      <option value="1">Start</option>\n                      <option value="2">Complete</option>\n                      <option value="3">Failed</option>\n                    </select>\n                  </div>\n                </div>\n\n                <div class="form-group enabledCheckbox">\n                  <label for="textfield" class="control-label col-sm-4">Enabled</label>\n                  <div class="col-sm-8">\n                    <input type="checkbox" name="chkEnabled" id="chkEnabled">\n                  </div>\n                </div>\n\n              </div>\n\n              <div class="col-sm-6">\n                <div class="form-group date-time" style="display:none;">\n                  <label for="textfield" class="control-label col-sm-4" id="lblDate">Date time</label>\n                  <div class="col-sm-4">\n                    <input type="text" name="txtDate" id="txtDate" data-date-format="yyyy/mm/dd"\n                      class="form-control datepick">\n                  </div>\n                  <div class="col-sm-4">\n                    <input type="text" name="txtTime" id="txtTime" class="form-control timepick">\n                  </div>\n                </div>\n\n                <div class="form-group run-model-days" style="display:none;">\n                  <label for="textfield" class="control-label col-sm-4">Days</label>\n                  <div class="col-sm-8">\n                    <div class="checkbox">\n                      <label>\n                        <input type="checkbox" name="checkbox" value="1">Sunday\n                      </label>\n                    </div>\n                    <div class="checkbox">\n                      <label>\n                        <input type="checkbox" name="checkbox" value="2">Monday\n                      </label>\n                    </div>\n\n                    <div class="checkbox">\n                      <label>\n                        <input type="checkbox" name="checkbox" value="3">Tuesday\n                      </label>\n                    </div>\n\n                    <div class="checkbox">\n                      <label>\n                        <input type="checkbox" name="checkbox" value="4">Wednesday\n                      </label>\n                    </div>\n                    <div class="checkbox">\n                      <label>\n                        <input type="checkbox" name="checkbox" value="5">Thursday\n                      </label>\n                    </div>\n                    <div class="checkbox">\n                      <label>\n                        <input type="checkbox" name="checkbox" value="6">Friday\n                      </label>\n                    </div>\n                    <div class="checkbox">\n                      <label>\n                        <input type="checkbox" name="checkbox" value="7">Saturday\n                      </label>\n                    </div>\n                  </div>\n                </div>\n\n              </div>\n            </div>\n          </div>\n          \x3c!-- END TAB 2 --\x3e\n\n          \x3c!-- START TAB 3 --\x3e\n          <div class="tab-pane" id="etl-3">\n            <div class="row">\n\n              <div class="col-sm-12">\n                <button class="btn btn-green add-param">Add param</button>\n\n                <table class="table table-hover table-nomargin paramList" width="100%">\n                  <thead>\n                    <tr>\n                      <th width="15%">'+r(l(t(668)).call(c,"_type",{name:"L",hash:{},data:o,loc:{start:{line:213,column:38},end:{line:213,column:51}}}))+'</th>\n                      <th width="20%">'+r(l(t(668)).call(c,"_name",{name:"L",hash:{},data:o,loc:{start:{line:214,column:38},end:{line:214,column:51}}}))+'</th>\n                      <th width="20%">'+r(l(t(668)).call(c,"_label",{name:"L",hash:{},data:o,loc:{start:{line:215,column:38},end:{line:215,column:52}}}))+'</th>\n                      <th width="15%">'+r(l(t(668)).call(c,"_default_value",{name:"L",hash:{},data:o,loc:{start:{line:216,column:38},end:{line:216,column:60}}}))+'</th>\n                      <th width="15%">'+r(l(t(668)).call(c,"actions",{name:"L",hash:{},data:o,loc:{start:{line:217,column:38},end:{line:217,column:53}}}))+'</th>\n                    </tr>\n                  </thead>\n                  <tbody>\n                  </tbody>\n                </table>\n              </div>\n\n            </div>\n          </div>\n          \x3c!-- END TAB 3 --\x3e\n\n          \x3c!-- START TAB 4 --\x3e\n          <div class="tab-pane" id="etl-4">\n\n            <div class="row">\n              <div class="col-sm-12">\n                <h5>On complete</h5>\n              </div>\n            </div>\n\n            <div class="row">\n              <div class="form-group">\n                <label for="textfield" class="control-label col-sm-2">Task name</label>\n                <div class="col-sm-10">\n                  <input type="text" class="relatedComplete" style="width:300px;">\n                </div>\n              </div>\n\n              <div class="relatedCompleteParams"></div>\n\n              <div class="form-group">\n                <label for="textfield" class="control-label col-sm-2">Enabled</label>\n                <div class="col-sm-10">\n                  <input type="checkbox" name="chkEnabledOk" class="chkEnabledComplete">\n                </div>\n              </div>\n\n            </div>\n\n            <div class="row">\n              <div class="col-sm-12">\n                <h5>On fail</h5>\n              </div>\n            </div>\n\n            <div class="row">\n              <div class="form-group">\n                <label for="textfield" class="control-label col-sm-2">Task name</label>\n                <div class="col-sm-10">\n                  <input type="text" class="relatedFail" style="width:300px;">\n                </div>\n              </div>\n\n              <div class="relatedFailParams"></div>\n\n              <div class="form-group">\n                <label for="textfield" class="control-label col-sm-2">Enabled</label>\n                <div class="col-sm-10">\n                  <input type="checkbox" name="chkEnabledError" class="chkEnabledFail">\n                </div>\n              </div>\n\n            </div>\n          </div>\n          \x3c!-- END TAB 4 --\x3e\n\n\n          <div class="row">\n            <div class="form-actions">\n              <button type="submit" class="btn btn-primary save">'+r(l(t(668)).call(c,"_save",{name:"L",hash:{},data:o,loc:{start:{line:287,column:65},end:{line:287,column:78}}}))+'</button>\n              <button type="button" class="btn cancel">'+r(l(t(668)).call(c,"_cancel",{name:"L",hash:{},data:o,loc:{start:{line:288,column:55},end:{line:288,column:70}}}))+"</button>\n            </div>\n          </div>\n\n        </div>\n      </div>\n\n    </div>\n  </div>\n\n</div>"},useData:!0})},713:function(e,n,t){"use strict";(function(a){var l,s=t(679);void 0===(l=function(){return a.Model.extend({list:function(e,n){(0,s.send)("users/?page=1",null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n)},listByCompany:function(e){(0,s.send)("usercompanies/list_by_company_id/",null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},e)},get:function(e,n){(0,s.send)("users/".concat(e,"/"),null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n)},update:function(e,n,t){(0,s.send)("users/".concat(e,"/"),n,{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},t)},partialUpdateUser:function(e,n,t){(0,s.send)("users/".concat(e,"/"),JSON.stringify(n),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},t)},EditProfile:function(e,n){(0,s.send)("users/".concat(e.id,"/"),JSON.stringify(e),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},n)},create:function(e,n){(0,s.send)("usercompanies/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},n)},partialUpdate:function(e,n,t){(0,s.send)("usercompanies/".concat(e,"/"),JSON.stringify(n),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},t)},deleteUser:function(e,n){(0,s.send)("users/".concat(e,"/"),null,{type:"DELETE"},n)},deleteUserCompany:function(e,n){(0,s.send)("usercompanies/".concat(e,"/"),null,{type:"DELETE"},n)},getUserCompany:function(e,n){(0,s.send)("usercompanies/".concat(e,"/"),null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n)},UpdateUserPreference:function(e,n){var t={userCompanyId:__currentSession.userId,preferenceCode:e,value:n};(0,s.send)("user/UpdateUserPreference",t,{type:"PUT"})},GetUserPreference:function(e,n){(0,s.send)("usercompanies/preference_by_code/?code=".concat(e),null,{type:"GET"},n)},GetRelatedDashboard:function(e){(0,s.send)("user/GetRelatedDashboard",null,null,e)}})}.apply(n,[]))||(e.exports=l)}).call(this,t(219))},739:function(e,n,t){"use strict";(function(a){var l,s=t(679);void 0===(l=function(){return a.Model.extend({url:"myFileManager",getTask:function(e,n){(0,s.send)("scheduler/".concat(e,"/"),null,{type:"GET"},n)},getTaskLog:function(e,n){(0,s.send)("taskLog/by_periodic_task/",e,{type:"POST"},n,null,!0)},filterLogs:function(e,n,t){(0,s.send)("taskLog/filter_logs/?page=".concat(e),JSON.stringify(n),{type:"POST",contentType:"application/json;charset=utf-8"},t,null,!0)},create:function(e,n,t){(0,s.send)("scheduler/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},n,t,!1,!0)},edit:function(e,n,t){(0,s.send)("scheduler/".concat(e.id,"/"),JSON.stringify(e),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},n,t,!1,!0)},partialEdit:function(e,n,t,a){(0,s.send)("scheduler/".concat(e,"/"),JSON.stringify(n),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},t,a,!1,!0)},list:function(e,n){(0,s.send)("scheduler/",null,{type:"GET"},e,n)},deleteTask:function(e,n){(0,s.send)("scheduler/".concat(e,"/"),null,{type:"DELETE"},n)},runTask:function(e,n){var t=e.periodic_task_id;e.scheduleTaskId;(0,s.send)("scheduler/".concat(t,"/runTask/"),null,{type:"POST"},n)},getPythonTimezones:function(e,n){(0,s.send)("scheduler/getPythonTimezones/",null,{type:"GET"},e,n)}})}.apply(n,[]))||(e.exports=l)}).call(this,t(219))}}]);
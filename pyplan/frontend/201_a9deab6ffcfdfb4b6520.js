/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[201,284],{2622:function(t,n,a){"use strict";(function(e,l){var s,i,o,r=a(18),c=(o=a(223))&&o.__esModule?o:{default:o};s=[a(748),a(739),a(2623)],void 0===(i=function(t,n,s){return e.View.extend({el:l("#main"),_uId:"",permisions:[],listToWatch:{values:[]},processLength:null,taskSchedulerModel:new n,taskSchedulerController:new t,render:function(){l("div[data-rel='"+this.options.taskType+"']").remove();var t=this;this._uId=l.uuid(),this.taskSchedulerModel.list((function(n){t.tasksList=n,n.forEach((function(n){t.listToWatch.values.push(n.id);var a=t.getStatusInfo(n.state);n.last_run_at?n.last_run_at=(0,c.default)(n.last_run_at).format("MM/DD/YYYY h:mm:ss a"):n.last_run_at="N/A",n.next_execution?n.nextRunDate=(0,c.default)(n.next_execution).format("MM/DD/YYYY h:mm:ss a"):n.nextRunDate="N/A",n.statusStr=a.statusStr,n.statusClass=a.statusClass,n.hasParams?(n.btnColor=n.hasParams?"btn-orange":"btn-green",n.hasParams=!!n.hasParams):(n.btnColor="btn-green",n.hasParams=!1)}));var a={tasks:n,id:t._uId,dataRel:t.options.taskType,tmpClass:t.options.taskType,title:"Model Tasks"},e=s(a);t.$el.append(e),t.view=l("div[data-id='"+t._uId+"']"),l("div[data-id='"+t._uId+"']").find("table").dataTable({fnRowCallback:function(n,a,e,s){this.fnGetPosition(n);return 0===l(n).find("div.multi-switch").length&&(l("td:eq(5) .multi-switch",n).multiSwitch(),l(n).find("div.multi-switch .switch-content:not(.disabled)").on("click",(function(n){t.updatePolicy(n,t)}))),n}}),l('<div class="actions data-table-options">').insertAfter(".dataTables_length");var i=l("div[data-id='"+t._uId+"']").find("div.data-table-options");function o(){var n=l(window).height();t.h=n-320,l("div[data-id='"+t._uId+"']").find(".dataTables_scrollBody").css("height",t.h+"px")}l('<button class="btn btn-green btn-addTask" task-type="'+t.options.taskType+'"><i class="fa fa-plus"></i> Add task </button>').appendTo(i),l(window).resize(o),o(),t.addHandlers(l("div[data-id='"+t._uId+"']")),t.view.find(".btn-addTask").on("click",(function(n){return n.preventDefault(),t.addTask(n,t),!1})),t.view.on("click",".btn-copy-task",(function(n){return n.preventDefault(),t.copyTask(n,t),!1})),t.view.on("click",".btn-edit-task",(function(n){return n.preventDefault(),t.editTask(n,t),!1})),t.view.on("click",".btn-delete-task",(function(n){return n.preventDefault(),t.deleteTask(n,t),!1})),t.view.on("click",".btn-log-task",(function(n){return n.preventDefault(),t.showLog(n,t),!1})),t.view.on("click",".btn-run-task",(function(n){return n.preventDefault(),t.run(n,t),!1})),t.view.on("click",".btn-stop-task",(function(n){return n.preventDefault(),t.stop(n,t),!1})),t.view.on("removeView",(function(){t.onRemoveView()})),t.poll=setInterval((function(){t.refreshTaskStates()}),7e3)}))},refreshTaskStates:function(){if(this.view.is(":visible"));},onRemoveView:function(){this.permisions=null,this.taskSchedulerModel=null,this.taskSchedulerController=null,this.listToWatch=null,clearInterval(this.poll)},getStatusInfo:function(t){var n={statusStr:null,statusClass:null};switch(t){case"PROGRESS":n.statusStr="Running",n.statusClass="warning";break;case"INFO":n.statusStr="Info",n.statusClass="info";break;case"WARNING":n.statusStr="Warning",n.statusClass="warning";break;case"FAILURE":n.statusStr="Failed",n.statusClass="danger";break;case"RETRY":n.statusStr="Retry",n.statusClass="warning";break;case"SUCCESS":n.statusStr="Completed",n.statusClass="success";break;case"REVOKED":n.statusStr="Revoked",n.statusClass="warning";break;case"STARTED":n.statusStr="Started",n.statusClass="warning";break;case"PENDING":n.statusStr="Pending",n.statusClass="warning";break;case"RECEIVED":n.statusStr="Received",n.statusClass="warning"}return n},updatePolicy:function(t,n){var a=!l(t.currentTarget).hasClass("active"),e=l(t.currentTarget).closest("tr").attr("schedule-task-id"),s={enabled:a};this.taskSchedulerModel.partialEdit(e,s,(function(n){l(t.currentTarget).closest("tr").find("button.btn-run-task").enable(a)}))},addTask:function(t,n){var e=l(t.currentTarget).attr("task-type");Promise.resolve().then((function(){var t=[a(748)];(function(t){(new t).addScheduleTask(null,e,n.tasksList)}).apply(null,t)})).catch(a.oe)},editTask:function(t,e){var s=l(t.currentTarget).parent().parent().attr("schedule-task-id");(new n).getTask(s,(function(t){Promise.resolve().then((function(){var n=[a(748)];(function(n){(new n).showRunModelTask(t)}).apply(null,n)})).catch(a.oe)}))},copyTask:function(t,a){var e=l(t.currentTarget).parent().parent().attr("schedule-task-id");(new n).copyTask(e,(function(t){a.render()}))},deleteTask:function(t,e){var s=l(t.currentTarget).parent().parent().attr("schedule-task-id");a.e(7).then((function(){var t=[a(663)];(function(t){(new t).show({title:(0,r.translate)("_delete_task"),text:(0,r.translate)("_delete_task_msg"),buttons:[{title:(0,r.translate)("cancel"),code:"no"},{title:(0,r.translate)("delete"),css:"red",code:"yes"}],callback:function(t){"yes"==t&&(new n).deleteTask(s,(function(){e.render()}))}})}).apply(null,t)})).catch(a.oe)},showLog:function(t,n){var a=l(t.currentTarget).closest("tr"),e={periodic_task_id:l(a).attr("schedule-task-id"),scheduleSubTask:null,scheduleTaskSessionId:0,hasParam:"true"===l(a).attr("has-param"),headerInfo:{}};n.taskSchedulerController.showTaskLogs(e)},run:function(t,e){var s=l(t.currentTarget).parent().parent().attr("schedule-task-id"),i=l(t.currentTarget).parent().parent().attr("has-param"),o=new n;"true"===i?a.e(75).then((function(){var t=[a(1652)];(function(t){(new t).render(s,e,e.onRunWithParams)}).apply(null,t)})).catch(a.oe):o.runTask({periodic_task_id:s},(function(t){if(t){var n=e.view.find('table tr[schedule-task-id="'+s+'"] td span');n.html((0,r.translate)("_running")),n.attr("class","label label-warning");e.view.find('table tr[schedule-task-id="'+s+'"]')}}))},stop:function(t,a){var e=l(t.currentTarget).parent().parent().attr("schedule-task-id"),s=new n;a=this;s.stopTask(e,(function(t){var n=a.view.find('table tr[schedule-task-id="'+e+'"]');t&&(n.find(".btn-stop-task").hide(),n.find(".btn-run-task").show(),a.refreshTaskStates())}))},onRunWithParams:function(t,a){a=a;var e=t.id;(new n).runTask({periodic_task_id:e},(function(t){if(t){var n=a.view.find('table tr[schedule-task-id="'+e+'"] td span');n.html((0,r.translate)("_running")),n.attr("class","label label-warning");a.view.find('table tr[schedule-task-id="'+e+'"]')}}))},cancel:function(t,n){var e=l("#currentTask").attr("data-rel");Promise.resolve().then((function(){var t=[a(664)];(function(t){clearInterval(n.poll),(new t).removeTask(e)}).apply(null,t)})).catch(a.oe)},addHandlers:function(t){var n=this;l("div[data-id='"+this._uId+"']").find("div.submit button.btn-cancel").on("click",l.proxy((function(){return this.cancel(),!1}),this)),l("div[data-id='"+this._uId+"']").find("div.abm-top-options a.btn-close").on("click",(function(t){return t.preventDefault(),n.cancel(t,n),!1}))}})}.apply(n,s))||(t.exports=i)}).call(this,a(219),a(1))},2623:function(t,n,a){var e=a(670);function l(t){return t&&(t.__esModule?t.default:t)}t.exports=(e.default||e).template({1:function(t,n,e,s,i){var o,r=t.lambda,c=t.escapeExpression,u=null!=n?n:t.nullContext||{},d=t.lookupProperty||function(t,n){if(Object.prototype.hasOwnProperty.call(t,n))return t[n]};return'              <tr schedule-task-id="'+c(r(null!=n?d(n,"id"):n,n))+'" has-param="'+c(r(null!=n?d(n,"hasParams"):n,n))+'" data-sortable="false">\n                <td>\n                  <strong>'+c(r(null!=n?d(n,"name"):n,n))+"</strong>\n                </td>\n                <td>\n                  "+c(r(null!=n?d(n,"created_by"):n,n))+"\n                </td>\n                <td>\n                  "+c(r(null!=n?d(n,"last_run_at"):n,n))+'\n                </td>\n                <td>\n                  <span class="label label-'+c(r(null!=n?d(n,"statusClass"):n,n))+'">'+c(r(null!=n?d(n,"statusStr"):n,n))+"</span>\n                </td>\n                <td>\n                  "+c(r(null!=n?d(n,"nextRunDate"):n,n))+"\n                </td>\n                <td>\n                  <center>\n"+(null!=(o=l(a(669)).call(u,null!=n?d(n,"scheduleRunType"):n,"==",4,{name:"ifCond",hash:{},fn:t.program(2,i,0),inverse:t.program(4,i,0),data:i,loc:{start:{line:46,column:20},end:{line:52,column:31}}}))?o:"")+'                  </center>\n                </td>\n\n                <td>\n\n                  \x3c!--button class="btn btn-small btn-copy-task" rel="tooltip" title=""\n                    data-original-title="'+c(l(a(668)).call(u,"_copy_task",{name:"L",hash:{},data:i,loc:{start:{line:59,column:41},end:{line:59,column:59}}}))+'"><i class="fa fa-files"></i></button--\x3e\n                  <button class="btn btn-small btn-edit-task" rel="tooltip" title=""\n                    data-original-title="'+c(l(a(668)).call(u,"_edit_task",{name:"L",hash:{},data:i,loc:{start:{line:61,column:41},end:{line:61,column:59}}}))+'"><i class="fa fa-pencil"></i></button>\n                  <button class="btn btn-small btn-delete-task" rel="tooltip" title=""\n                    data-original-title="'+c(l(a(668)).call(u,"_delete_task",{name:"L",hash:{},data:i,loc:{start:{line:63,column:41},end:{line:63,column:61}}}))+'"><i class="fa fa-trash"></i></button>\n\n                  <button class="btn btn-small btn-log-task" rel="tooltip" title=""\n                    data-original-title="'+c(l(a(668)).call(u,"_watch_task_log",{name:"L",hash:{},data:i,loc:{start:{line:66,column:41},end:{line:66,column:64}}}))+'"><i class="fa fa-list-alt"></i></button>\n\n'+(null!=(o=l(a(669)).call(u,null!=n?d(n,"scheduleRunType"):n,"==",4,{name:"ifCond",hash:{},fn:t.program(7,i,0),inverse:t.program(9,i,0),data:i,loc:{start:{line:68,column:18},end:{line:74,column:29}}}))?o:"")+'\n                  <button class="btn btn-small btn-red btn-stop-task nodisplay"><i class="fa fa-stop-circle-o"></i>\n                    '+c(l(a(668)).call(u,"stop",{name:"L",hash:{},data:i,loc:{start:{line:77,column:20},end:{line:77,column:32}}}))+" </button>\n                </td>\n\n              </tr>\n\n"},2:function(t,n,a,e,l){return"                    Manual\n"},4:function(t,n,e,s,i){var o,r=t.lookupProperty||function(t,n){if(Object.prototype.hasOwnProperty.call(t,n))return t[n]};return'\n                    <input type="checkbox" class="multi-switch" data-format-key="bottomTotal"\n                      '+(null!=(o=l(a(669)).call(null!=n?n:t.nullContext||{},null!=n?r(n,"enabled"):n,"==",!0,{name:"ifCond",hash:{},fn:t.program(5,i,0),inverse:t.noop,data:i,loc:{start:{line:51,column:22},end:{line:51,column:81}}}))?o:"")+" />\n"},5:function(t,n,a,e,l){return' checked="checked" '},7:function(t,n,e,s,i){var o=t.escapeExpression,r=t.lookupProperty||function(t,n){if(Object.prototype.hasOwnProperty.call(t,n))return t[n]};return'                  <button class="btn btn-small '+o(t.lambda(null!=n?r(n,"btnColor"):n,n))+' btn-run-task"><i class="fa fa-caret-right"></i> '+o(l(a(668)).call(null!=n?n:t.nullContext||{},"_run",{name:"L",hash:{},data:i,loc:{start:{line:69,column:108},end:{line:69,column:120}}}))+"\n                  </button>\n"},9:function(t,n,e,s,i){var o,r=t.escapeExpression,c=null!=n?n:t.nullContext||{},u=t.lookupProperty||function(t,n){if(Object.prototype.hasOwnProperty.call(t,n))return t[n]};return'                  <button class="btn btn-small '+r(t.lambda(null!=n?u(n,"btnColor"):n,n))+' btn-run-task" '+(null!=(o=l(a(669)).call(c,null!=n?u(n,"enabled"):n,"==",!1,{name:"ifCond",hash:{},fn:t.program(10,i,0),inverse:t.noop,data:i,loc:{start:{line:72,column:74},end:{line:73,column:51}}}))?o:"")+'><i class="fa fa-caret-right"></i> '+r(l(a(668)).call(c,"_run",{name:"L",hash:{},data:i,loc:{start:{line:73,column:86},end:{line:73,column:98}}}))+" </button>\n"},10:function(t,n,a,e,l){return'\n                    disabled="disabled" '},compiler:[8,">= 4.3.0"],main:function(t,n,e,s,i){var o,r=t.lambda,c=t.escapeExpression,u=null!=n?n:t.nullContext||{},d=t.lookupProperty||function(t,n){if(Object.prototype.hasOwnProperty.call(t,n))return t[n]};return'<div class="abm-base-tmp '+c(r(null!=n?d(n,"tmpClass"):n,n))+' container-fluid mainTask" data-id="'+c(r(null!=n?d(n,"id"):n,n))+'" data-rel="'+c(r(null!=n?d(n,"dataRel"):n,n))+'"\n  data-type="tab-content">\n  <div class="row">\n    <div class="col-sm-12">\n      <div class="box">\n        <div class="box-title">\n          <h3><i class="fa fa-th-list"></i>'+c(r(null!=n?d(n,"title"):n,n))+'</h3>\n          <div class="actions abm-top-options">\n            <a href="#" class="btn btn-close"><i class="fa fa-times"></i></a>\n          </div>\n        </div>\n        <div class="box-content nopadding abm-content">\n\n          <table class="table table-hover table-condensed dataTable dataTable-scroll-x etlTasks dataTable-nosort">\n            <thead>\n              <tr>\n                <th width="20%">'+c(l(a(668)).call(u,"_name",{name:"L",hash:{},data:i,loc:{start:{line:17,column:32},end:{line:17,column:45}}}))+'</th>\n                <th width="12%">'+c(l(a(668)).call(u,"_created_by",{name:"L",hash:{},data:i,loc:{start:{line:18,column:32},end:{line:18,column:51}}}))+'</th>\n                <th width="12%">'+c(l(a(668)).call(u,"_last_execution",{name:"L",hash:{},data:i,loc:{start:{line:19,column:32},end:{line:19,column:55}}}))+'</th>\n                <th width="12%">'+c(l(a(668)).call(u,"_last_status",{name:"L",hash:{},data:i,loc:{start:{line:20,column:32},end:{line:20,column:52}}}))+'</th>\n                <th width="12%">'+c(l(a(668)).call(u,"_next_execution",{name:"L",hash:{},data:i,loc:{start:{line:21,column:32},end:{line:21,column:55}}}))+'</th>\n                <th width="10%">'+c(l(a(668)).call(u,"_enabled",{name:"L",hash:{},data:i,loc:{start:{line:22,column:32},end:{line:22,column:48}}}))+'</th>\n                <th width="22%">'+c(l(a(668)).call(u,"_options",{name:"L",hash:{},data:i,loc:{start:{line:23,column:32},end:{line:23,column:48}}}))+"</th>\n              </tr>\n            </thead>\n            <tbody>\n"+(null!=(o=d(e,"each").call(u,null!=n?d(n,"tasks"):n,{name:"each",hash:{},fn:t.program(1,i,0),inverse:t.noop,data:i,loc:{start:{line:27,column:14},end:{line:82,column:23}}}))?o:"")+"            </tbody>\n          </table>\n        </div>\n      </div>\n    </div>\n  </div>\n</div>"},useData:!0})},739:function(t,n,a){"use strict";(function(e){var l,s=a(679);void 0===(l=function(){return e.Model.extend({url:"myFileManager",getTask:function(t,n){(0,s.send)("scheduler/".concat(t,"/"),null,{type:"GET"},n)},getTaskLog:function(t,n){(0,s.send)("taskLog/by_periodic_task/",t,{type:"POST"},n,null,!0)},filterLogs:function(t,n,a){(0,s.send)("taskLog/filter_logs/?page=".concat(t),JSON.stringify(n),{type:"POST",contentType:"application/json;charset=utf-8"},a,null,!0)},create:function(t,n,a){(0,s.send)("scheduler/",JSON.stringify(t),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},n,a,!1,!0)},edit:function(t,n,a){(0,s.send)("scheduler/".concat(t.id,"/"),JSON.stringify(t),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},n,a,!1,!0)},partialEdit:function(t,n,a,e){(0,s.send)("scheduler/".concat(t,"/"),JSON.stringify(n),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},a,e,!1,!0)},list:function(t,n){(0,s.send)("scheduler/",null,{type:"GET"},t,n)},deleteTask:function(t,n){(0,s.send)("scheduler/".concat(t,"/"),null,{type:"DELETE"},n)},runTask:function(t,n){var a=t.periodic_task_id;t.scheduleTaskId;(0,s.send)("scheduler/".concat(a,"/runTask/"),null,{type:"POST"},n)},getPythonTimezones:function(t,n){(0,s.send)("scheduler/getPythonTimezones/",null,{type:"GET"},t,n)}})}.apply(n,[]))||(t.exports=l)}).call(this,a(219))}}]);
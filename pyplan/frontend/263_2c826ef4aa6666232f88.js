/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[263,32,281],{1329:function(t,n,a){"use strict";(function(e,o){var l,s;l=[a(704),a(707),a(750),a(710),a(725),a(2042)],void 0===(s=function(t,n,l,s,i,r){return e.View.extend({el:o("#main"),_uId:"",permisions:[],processLength:null,workflowModel:new n,workflowController:new t,render:function(t){o("div[data-rel='abm-transitions-rol']").remove();var n=this;this._uId=o.uuid(),this.workflowModel.listTransitions(function(a){var e={id:n._uId,dataRel:"abm-transitions-rol",tmpClass:"rol-edit",title:"Transitions by rol"},l={transitions:a},d=s(e),u=i(),c=r(l);function p(){var t=o(window).height();n.h=t-320,o("div[data-id='"+n._uId+"']").find(".dataTables_scrollBody").css("height",n.h+"px")}n.$el.append(d),o("div[data-id='"+n._uId+"']").find("div.abm-content").append(u),o("div[data-id='"+n._uId+"']").find("div.form-content").append(c),t&&o("div[data-rel='abm-transitions-rol']").css("display","none"),n.addHandlers(o("div[data-id='"+n._uId+"']")),n.initRoles(a),o(window).resize(p),p()})},initRoles:function(t){var n=this,a=__currentSession.companyId;(new l).List(a,function(a){if(a.length>0){for(var e,l=[],s=[{value:"",text:""}],i=0;i<a.length;i++)s[i]={value:a[i].rolId,text:a[i].name},l.push(a[i].rolId);o("div[data-id='"+n._uId+"']").find("table").dataTable({fnRowCallback:function(n,a,l,i){e=[];for(var r=this.fnGetPosition(n),d=0;d<t[r].roles.length;d++)e.push(t[r].roles[d].rolId);return o("td:eq(1) a",n).attr("data-value",e.toString()),o("td:eq(1) a",n).editable({pk:1,value:e,source:s,mode:"inline",success:function(t,n){o(this).attr("data-value",n)}}),n}})}})},refreshList:function(t){var n=o('div[data-rel="abm-transitions-rol"]').find("table tbody").empty();(n=o('div[data-rel="abm-transitions-rol"] .processByRol').dataTable()).fnClearTable(),n.fnDestroy(),o("div[data-rel='abm-transitions-rol'] .processByRol").remove();var a=r({transitions:t});o("div[data-rel='abm-transitions-rol']").find("div.form-content").append(a),o("div[data-rel='abm-transitions-rol']").find("table").cubeTable(),this.addHandlers(o("div[data-rel='abm-transitions-rol']"))},save:function(t){var n,a={values:[]};o("div[data-id='"+(t=this)._uId+"']").find("table").DataTable().rows().nodes().each(function(t,e){var l=t,s=o(l).attr("from-id"),i=o(l).attr("to-id"),r=o(l).attr("transition-id");n={taskTransitionId:r,fromStateId:s,toStateId:i,roles:[]};var d=o(l).find("a.editable").attr("data-value");if(d&&d.length>0)for(var u=d.split(","),c=0;c<u.length;c++){var p={rolId:u[c]};n.roles.push(p)}a.values.push(n)}),t.workflowModel.updateRolTransitions(a,function(n){t.cancel()})},cancel:function(){var t=o("#currentTask").attr("data-rel");Promise.resolve().then(function(){var n=[a(684)];(function(n){(new n).removeTask(t)}).apply(null,n)}).catch(a.oe)},addHandlers:function(t){var n=this;o("div[data-id='"+this._uId+"']").find("form").on("submit",o.proxy(function(){return event.preventDefault(),this.save(n),!1},this)),o("div[data-id='"+this._uId+"']").find("div.submit button.btn-cancel").on("click",o.proxy(function(){return this.cancel(),!1},this)),o("div[data-id='"+this._uId+"']").find("div.abm-top-options a.btn-close").on("click",this.cancel)}})}.apply(n,l))||(t.exports=s)}).call(this,a(218),a(1))},2042:function(t,n,a){var e=a(690);t.exports=(e.default||e).template({1:function(t,n,a,e,o){var l,s,i=null!=n?n:t.nullContext||{},r=a.helperMissing,d="function",u=t.escapeExpression;return'                <tr from-id="'+u(typeof(s=null!=(s=a.fromStateId||(null!=n?n.fromStateId:n))?s:r)===d?s.call(i,{name:"fromStateId",hash:{},data:o}):s)+'" to-id="'+u(typeof(s=null!=(s=a.toStateId||(null!=n?n.toStateId:n))?s:r)===d?s.call(i,{name:"toStateId",hash:{},data:o}):s)+'" transition-id="'+u(typeof(s=null!=(s=a.taskTransitionId||(null!=n?n.taskTransitionId:n))?s:r)===d?s.call(i,{name:"taskTransitionId",hash:{},data:o}):s)+'" data-sortable="false">\n                  <td>\n                    From <strong>'+u(typeof(s=null!=(s=a.fromStateName||(null!=n?n.fromStateName:n))?s:r)===d?s.call(i,{name:"fromStateName",hash:{},data:o}):s)+"</strong> to <strong>"+u(typeof(s=null!=(s=a.toStateName||(null!=n?n.toStateName:n))?s:r)===d?s.call(i,{name:"toStateName",hash:{},data:o}):s)+'</strong>\n                  </td>\n\n                  <td>\n                    <a href="#" class="editable editable-click rolesList" data-type="checklist" data-original-title=\'Roles\'>\n'+(null!=(l=a.each.call(i,null!=n?n.roles:n,{name:"each",hash:{},fn:t.program(2,o,0),inverse:t.noop,data:o}))?l:"")+"                    </a>\n                  </td>\n\n                </tr>\n\n"},2:function(t,n,a,e,o){var l,s=null!=n?n:t.nullContext||{},i=a.helperMissing,r=t.escapeExpression;return'                            <div data-value="'+r("function"==typeof(l=null!=(l=a.rolId||(null!=n?n.rolId:n))?l:i)?l.call(s,{name:"rolId",hash:{},data:o}):l)+'">'+r("function"==typeof(l=null!=(l=a.name||(null!=n?n.name:n))?l:i)?l.call(s,{name:"name",hash:{},data:o}):l)+"</div>\n"},compiler:[7,">= 4.0.0"],main:function(t,n,a,e,o){var l;return'\n\n          <table class="table table-hover table-condensed dataTable dataTable-scroll-x processByRol dataTable-nosort">\n            <thead>\n              <tr>\n                <th width="60%">Transitions</th>\n                <th width="40%">Roles</th>\n              </tr>\n            </thead>\n            <tbody>\n'+(null!=(l=a.each.call(null!=n?n:t.nullContext||{},null!=n?n.transitions:n,{name:"each",hash:{},fn:t.program(1,o,0),inverse:t.noop,data:o}))?l:"")+"            </tbody>\n          </table>\n"},useData:!0})},707:function(t,n,a){"use strict";(function(e){var o,l=a(693);void 0===(o=function(){return e.Model.extend({url:"myFileManager",getWorkflow:function(t,n){var a="Workflow/getWorkflow";t&&(a="Workflow/getWorkflow/"+t),(0,l.send)(a,null,{type:"GET"},n)},createTask:function(t,n){(0,l.send)("Workflow/createTask",t,{type:"POST"},n)},updateTask:function(t,n){(0,l.send)("Workflow/updateTask",t,{type:"PUT"},n)},updateTasksProperty:function(t,n){(0,l.send)("Workflow/updateTasksProperty",t,{type:"PUT"},n)},deleteTask:function(t,n){(0,l.send)("Workflow/deleteTask/"+t,null,{type:"DELETE"},n)},getTask:function(t,n){(0,l.send)("Workflow/getTask/"+t,null,null,n)},createState:function(t,n){(0,l.send)("Workflow/createState/",t,{type:"POST"},n)},listStates:function(t){(0,l.send)("Workflow/listStates",null,{type:"GET"},t)},getState:function(t,n){(0,l.send)("Workflow/getState/"+t,null,{type:"GET"},n)},updateState:function(t,n){(0,l.send)("Workflow/updateState",t,{type:"PUT"},n)},deleteState:function(t,n){(0,l.send)("Workflow/deleteState/"+t,null,{type:"DELETE"},n)},listTransitions:function(t){(0,l.send)("Workflow/listTransitions",null,{type:"GET"},t)},createTransition:function(t,n){(0,l.send)("Workflow/createTransition",t,{type:"POST"},n)},updateTransition:function(t,n){(0,l.send)("Workflow/updateTransition",t,{type:"PUT"},n)},deleteTransition:function(t,n){(0,l.send)("Workflow/deleteTransition/"+t,null,{type:"DELETE"},n)},listUsers:function(t){(0,l.send)("Workflow/listUsers",null,null,t)},getTaskGroup:function(t,n){(0,l.send)("Workflow/getTaskGroup/"+t,null,{type:"GET"},n)},listTaskGroups:function(t){(0,l.send)("Workflow/listTaskGroups",null,{type:"GET"},t)},createTaskGroup:function(t,n){(0,l.send)("Workflow/createTaskGroup",t,{type:"POST"},n)},updateTaskGroup:function(t,n){(0,l.send)("Workflow/updateTaskGroup",t,{type:"PUT"},n)},deleteTaskGroup:function(t,n){(0,l.send)("Workflow/DeleteTaskGroup/"+t,null,{type:"DELETE"},n)},updateOrder:function(t,n){(0,l.send)("Workflow/ChangeOrder",{values:t},{type:"PUT"},n)},updateRolTransitions:function(t,n){(0,l.send)("Workflow/updateRolTransitions",t,{type:"PUT"},n)},getWorkflowByGroups:function(t,n){(0,l.send)("Workflow/getWorkflowByGroups/",{values:t},{type:"POST"},n)},createComment:function(t,n){(0,l.send)("Workflow/createComment/",t,{type:"POST"},n)}})}.apply(n,[]))||(t.exports=o)}).call(this,a(218))},710:function(t,n,a){var e=a(690);t.exports=(e.default||e).template({compiler:[7,">= 4.0.0"],main:function(t,n,a,e,o){var l,s=null!=n?n:t.nullContext||{},i=a.helperMissing,r=t.escapeExpression;return'<div class="abm-base-tmp '+r("function"==typeof(l=null!=(l=a.tmpClass||(null!=n?n.tmpClass:n))?l:i)?l.call(s,{name:"tmpClass",hash:{},data:o}):l)+' container-fluid mainTask" data-id="'+r("function"==typeof(l=null!=(l=a.id||(null!=n?n.id:n))?l:i)?l.call(s,{name:"id",hash:{},data:o}):l)+'" data-rel="'+r("function"==typeof(l=null!=(l=a.dataRel||(null!=n?n.dataRel:n))?l:i)?l.call(s,{name:"dataRel",hash:{},data:o}):l)+'" data-type="tab-content">\n    <div class="row">\n        <div class="col-sm-12">\n            <div class="box">\n                <div class="box-title">\n                    <h3><i class="fa fa-th-list"></i>'+r("function"==typeof(l=null!=(l=a.title||(null!=n?n.title:n))?l:i)?l.call(s,{name:"title",hash:{},data:o}):l)+'</h3>\n                    <div class="actions abm-top-options">\n                        <a href="#" class="btn btn-close"><i class="fa fa-times"></i></a>\n                    </div>\n                </div>\n        <div class="box-content nopadding abm-content">\n\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n'},useData:!0})},725:function(t,n,a){var e=a(690);function o(t){return t&&(t.__esModule?t.default:t)}t.exports=(e.default||e).template({compiler:[7,">= 4.0.0"],main:function(t,n,e,l,s){var i=null!=n?n:t.nullContext||{},r=t.escapeExpression;return'<form action="#" id="baseForm" method="POST" class=\'form-horizontal form-bordered form-validate\' novalidate="novalidate">\n    <div class="form-content">\n\n    </div>\n    <div class="submit form-actions col-sm-12">\n        <button type="submit" class="btn btn-primary btn-save">'+r(o(a(688)).call(i,"_save",{name:"L",hash:{},data:s}))+'</button>\n        <button type="button" class="btn btn-cancel">'+r(o(a(688)).call(i,"cancel",{name:"L",hash:{},data:s}))+"</button>\n    </div>\n</form>\n"},useData:!0})},750:function(t,n,a){"use strict";(function(e){var o,l=a(693);void 0===(o=function(){return e.Model.extend({list:function(t,n){var a=null!=t?"?company_id=".concat(t):"";(0,l.send)("groups/".concat(a),null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n)},get:function(t,n){(0,l.send)("groups/".concat(t,"/"),null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n)},update:function(t,n,a){(0,l.send)("groups/".concat(t,"/"),JSON.stringify(n),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},a)},create:function(t,n){(0,l.send)("groups/",JSON.stringify(t),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},n)},delete:function(t,n){(0,l.send)("groups/".concat(t,"/"),null,{type:"DELETE"},n)},listPermissions:function(t){(0,l.send)("permissions/",null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},t)},updateGroupPermissions:function(t,n){(0,l.send)("groups/update_groups_permissions/",JSON.stringify(t),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},n)}})}.apply(n,[]))||(t.exports=o)}).call(this,a(218))}}]);
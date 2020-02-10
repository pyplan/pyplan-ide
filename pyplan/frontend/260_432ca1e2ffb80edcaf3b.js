/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[260,33],{1327:function(t,n,e){"use strict";(function(a,o){var l,i;l=[e(684),e(703),e(707),e(710),e(725),e(2038)],void 0===(i=function(t,n,l,i,s,r){return a.View.extend({el:o("#main"),_uId:"",permisions:[],processLength:null,workflowModel:new l,workflowController:new n,render:function(n){o("div[data-rel='abm-transitions']").remove();var e=this;this._uId=o.uuid();var a=new t;a.hideAllTasks(),a.selectTask("abm-transitions"),this.workflowModel.listStates(function(t){var a={id:e._uId,dataRel:"abm-transitions",tmpClass:"rol-edit",title:"Transitions Manager"},l={states:t,allStates:t},d=i(a),c=s(),u=r(l);function f(){var t=o(window).height();e.h=t-320,o("div[data-id='"+e._uId+"']").find(".dataTables_scrollBody")&&o("div[data-id='"+e._uId+"']").find(".dataTables_scrollBody").css("height",e.h+"px")}e.$el.append(d),o("div[data-id='"+e._uId+"']").find("div.abm-content").append(c),o("div[data-id='"+e._uId+"']").find("div.form-content").append(u),n&&o("div[data-rel='abm-transitions']").css("display","none"),o("div[data-id='"+e._uId+"']").find("table").cubeTable(),e.initCheckboxes(o("div[data-id='"+e._uId+"']")),e.addHandlers(o("div[data-id='"+e._uId+"']")),o(window).resize(f),f(),e.getThis().on("beforeRemoveView",function(t,n){e.onBeforeRemoveView(t,n)})})},refreshList:function(t){var n=o('div[data-rel="abm-transitions"]').find("table tbody").empty();(n=o('div[data-rel="abm-transitions"] .processByRol').dataTable()).fnClearTable(),n.fnDestroy(),o("div[data-rel='abm-transitions'] .processByRol").remove();var e=r({states:t,allStates:t});o("div[data-rel='abm-transitions']").find("div.form-content").append(e),o("div[data-rel='abm-transitions']").find("table").cubeTable(),this.initCheckboxes(o("div[data-rel='abm-transitions']")),this.addHandlers(o("div[data-rel='abm-transitions']"))},save:function(t){var n,e;(t=this).workflowModel.listTransitions(function(a){o("div[data-id='"+t._uId+"']").find("input.transition").each(function(){if(e=!1,o(this).prop("checked")){for(var l=0;l<a.length;l++)o(this).attr("data-from")===a[l].fromStateId.toString()&&o(this).attr("data-to")===a[l].toStateId.toString()&&(e=!0);e||(n={fromStateId:o(this).attr("data-from"),toStateId:o(this).attr("data-to")},t.workflowModel.createTransition(n,function(){}))}else for(var i=0;i<a.length;i++)o(this).attr("data-from")===a[i].fromStateId.toString()&&o(this).attr("data-to")===a[i].toStateId.toString()&&t.workflowModel.deleteTransition(a[i].taskTransitionId,function(){})}),t.cancel()})},cancel:function(){var t=o("#currentTask").attr("data-rel");Promise.resolve().then(function(){var n=[e(684)];(function(n){(new n).removeTask(t)}).apply(null,n)}).catch(e.oe)},addHandlers:function(t){var n=this;o("div[data-id='"+this._uId+"']").find("form").on("submit",o.proxy(function(){return this.save(n),!1},this)),o("div[data-id='"+this._uId+"']").find("div.submit button.btn-cancel").on("click",o.proxy(function(){return this.cancel(),!1},this)),o("div[data-id='"+this._uId+"']").find("div.abm-top-options a.btn-close").on("click",this.cancel)},getThis:function(){return this.$el.find(".mainTask[data-rel='abm-transitions']")},onBeforeRemoveView:function(t,n){var e=o('div[data-rel="abm-transitions"] .processByRol').dataTable();e.fnClearTable(),e.fnDestroy()},initCheckboxes:function(t){var n=this;this.workflowModel.listTransitions(function(t){for(var e=0;e<t.length;e++){var a=t[e].fromStateId,l=t[e].toStateId;o("div[data-id='"+n._uId+"']").find('input.transition[data-from="'+a+'"][data-to="'+l+'"]').prop("checked","checked")}})}})}.apply(n,l))||(t.exports=i)}).call(this,e(218),e(1))},2038:function(t,n,e){var a=e(690);t.exports=(a.default||a).template({1:function(t,n,e,a,o){var l,i=null!=n?n:t.nullContext||{},s=t.hooks.helperMissing,r=t.escapeExpression;return'                  <th data-rolId="'+r("function"==typeof(l=null!=(l=e.rolId||(null!=n?n.rolId:n))?l:s)?l.call(i,{name:"rolId",hash:{},data:o,loc:{start:{line:9,column:34},end:{line:9,column:43}}}):l)+'" class="chkAllHeader">\n                    '+r("function"==typeof(l=null!=(l=e.name||(null!=n?n.name:n))?l:s)?l.call(i,{name:"name",hash:{},data:o,loc:{start:{line:10,column:20},end:{line:10,column:28}}}):l)+"\n                  </th>\n"},3:function(t,n,e,a,o,l,i){var s,r,d=null!=n?n:t.nullContext||{},c=t.hooks.helperMissing,u=t.escapeExpression;return'                <tr data-groupCode="'+u("function"==typeof(r=null!=(r=e.code||(null!=n?n.code:n))?r:c)?r.call(d,{name:"code",hash:{},data:o,loc:{start:{line:17,column:36},end:{line:17,column:44}}}):r)+'" data-sortable="false">\n                  <td>\n                    <strong>'+u("function"==typeof(r=null!=(r=e.name||(null!=n?n.name:n))?r:c)?r.call(d,{name:"name",hash:{},data:o,loc:{start:{line:19,column:28},end:{line:19,column:36}}}):r)+"</strong>\n                  </td>\n"+(null!=(s=e.each.call(d,null!=i[1]?i[1].allStates:i[1],{name:"each",hash:{},fn:t.program(4,o,0,l,i),inverse:t.noop,data:o,loc:{start:{line:21,column:18},end:{line:28,column:27}}}))?s:"")+"                </tr>\n\n"},4:function(t,n,e,a,o,l,i){var s,r=t.escapeExpression;return'                    <td style="text-align:center;">\n                      <input type="checkbox" class="transition"\n                      data-from="'+r(t.lambda(null!=i[1]?i[1].taskStateId:i[1],n))+'"\n                      data-to="'+r("function"==typeof(s=null!=(s=e.taskStateId||(null!=n?n.taskStateId:n))?s:t.hooks.helperMissing)?s.call(null!=n?n:t.nullContext||{},{name:"taskStateId",hash:{},data:o,loc:{start:{line:25,column:31},end:{line:25,column:46}}}):s)+'"\n                       />\n                    </td>\n'},compiler:[8,">= 4.3.0"],main:function(t,n,e,a,o,l,i){var s,r=null!=n?n:t.nullContext||{};return'\n\n          <table class="table table-hover table-condensed dataTable dataTable-scroll-x processByRol dataTable-nosort">\n            <thead>\n              <tr>\n                <th>Status</th>\n\n'+(null!=(s=e.each.call(r,null!=n?n.states:n,{name:"each",hash:{},fn:t.program(1,o,0,l,i),inverse:t.noop,data:o,loc:{start:{line:8,column:16},end:{line:12,column:25}}}))?s:"")+"              </tr>\n            </thead>\n            <tbody>\n"+(null!=(s=e.each.call(r,null!=n?n.states:n,{name:"each",hash:{},fn:t.program(3,o,0,l,i),inverse:t.noop,data:o,loc:{start:{line:16,column:14},end:{line:31,column:23}}}))?s:"")+"            </tbody>\n          </table>\n"},useData:!0,useDepths:!0})},707:function(t,n,e){"use strict";(function(a){var o,l=e(693);void 0===(o=function(){return a.Model.extend({url:"myFileManager",getWorkflow:function(t,n){var e="Workflow/getWorkflow";t&&(e="Workflow/getWorkflow/"+t),(0,l.send)(e,null,{type:"GET"},n)},createTask:function(t,n){(0,l.send)("Workflow/createTask",t,{type:"POST"},n)},updateTask:function(t,n){(0,l.send)("Workflow/updateTask",t,{type:"PUT"},n)},updateTasksProperty:function(t,n){(0,l.send)("Workflow/updateTasksProperty",t,{type:"PUT"},n)},deleteTask:function(t,n){(0,l.send)("Workflow/deleteTask/"+t,null,{type:"DELETE"},n)},getTask:function(t,n){(0,l.send)("Workflow/getTask/"+t,null,null,n)},createState:function(t,n){(0,l.send)("Workflow/createState/",t,{type:"POST"},n)},listStates:function(t){(0,l.send)("Workflow/listStates",null,{type:"GET"},t)},getState:function(t,n){(0,l.send)("Workflow/getState/"+t,null,{type:"GET"},n)},updateState:function(t,n){(0,l.send)("Workflow/updateState",t,{type:"PUT"},n)},deleteState:function(t,n){(0,l.send)("Workflow/deleteState/"+t,null,{type:"DELETE"},n)},listTransitions:function(t){(0,l.send)("Workflow/listTransitions",null,{type:"GET"},t)},createTransition:function(t,n){(0,l.send)("Workflow/createTransition",t,{type:"POST"},n)},updateTransition:function(t,n){(0,l.send)("Workflow/updateTransition",t,{type:"PUT"},n)},deleteTransition:function(t,n){(0,l.send)("Workflow/deleteTransition/"+t,null,{type:"DELETE"},n)},listUsers:function(t){(0,l.send)("Workflow/listUsers",null,null,t)},getTaskGroup:function(t,n){(0,l.send)("Workflow/getTaskGroup/"+t,null,{type:"GET"},n)},listTaskGroups:function(t){(0,l.send)("Workflow/listTaskGroups",null,{type:"GET"},t)},createTaskGroup:function(t,n){(0,l.send)("Workflow/createTaskGroup",t,{type:"POST"},n)},updateTaskGroup:function(t,n){(0,l.send)("Workflow/updateTaskGroup",t,{type:"PUT"},n)},deleteTaskGroup:function(t,n){(0,l.send)("Workflow/DeleteTaskGroup/"+t,null,{type:"DELETE"},n)},updateOrder:function(t,n){(0,l.send)("Workflow/ChangeOrder",{values:t},{type:"PUT"},n)},updateRolTransitions:function(t,n){(0,l.send)("Workflow/updateRolTransitions",t,{type:"PUT"},n)},getWorkflowByGroups:function(t,n){(0,l.send)("Workflow/getWorkflowByGroups/",{values:t},{type:"POST"},n)},createComment:function(t,n){(0,l.send)("Workflow/createComment/",t,{type:"POST"},n)}})}.apply(n,[]))||(t.exports=o)}).call(this,e(218))},710:function(t,n,e){var a=e(690);t.exports=(a.default||a).template({compiler:[8,">= 4.3.0"],main:function(t,n,e,a,o){var l,i=null!=n?n:t.nullContext||{},s=t.hooks.helperMissing,r=t.escapeExpression;return'<div class="abm-base-tmp '+r("function"==typeof(l=null!=(l=e.tmpClass||(null!=n?n.tmpClass:n))?l:s)?l.call(i,{name:"tmpClass",hash:{},data:o,loc:{start:{line:1,column:25},end:{line:1,column:37}}}):l)+' container-fluid mainTask" data-id="'+r("function"==typeof(l=null!=(l=e.id||(null!=n?n.id:n))?l:s)?l.call(i,{name:"id",hash:{},data:o,loc:{start:{line:1,column:73},end:{line:1,column:79}}}):l)+'" data-rel="'+r("function"==typeof(l=null!=(l=e.dataRel||(null!=n?n.dataRel:n))?l:s)?l.call(i,{name:"dataRel",hash:{},data:o,loc:{start:{line:1,column:91},end:{line:1,column:102}}}):l)+'" data-type="tab-content">\n    <div class="row">\n        <div class="col-sm-12">\n            <div class="box">\n                <div class="box-title">\n                    <h3><i class="fa fa-th-list"></i>'+r("function"==typeof(l=null!=(l=e.title||(null!=n?n.title:n))?l:s)?l.call(i,{name:"title",hash:{},data:o,loc:{start:{line:6,column:53},end:{line:6,column:62}}}):l)+'</h3>\n                    <div class="actions abm-top-options">\n                        <a href="#" class="btn btn-close"><i class="fa fa-times"></i></a>\n                    </div>\n                </div>\n        <div class="box-content nopadding abm-content">\n\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n'},useData:!0})},725:function(t,n,e){var a=e(690);function o(t){return t&&(t.__esModule?t.default:t)}t.exports=(a.default||a).template({compiler:[8,">= 4.3.0"],main:function(t,n,a,l,i){var s=null!=n?n:t.nullContext||{},r=t.escapeExpression;return'<form action="#" id="baseForm" method="POST" class=\'form-horizontal form-bordered form-validate\' novalidate="novalidate">\n    <div class="form-content">\n\n    </div>\n    <div class="submit form-actions col-sm-12">\n        <button type="submit" class="btn btn-primary btn-save">'+r(o(e(688)).call(s,"_save",{name:"L",hash:{},data:i,loc:{start:{line:6,column:63},end:{line:6,column:76}}}))+'</button>\n        <button type="button" class="btn btn-cancel">'+r(o(e(688)).call(s,"cancel",{name:"L",hash:{},data:i,loc:{start:{line:7,column:53},end:{line:7,column:67}}}))+"</button>\n    </div>\n</form>\n"},useData:!0})}}]);
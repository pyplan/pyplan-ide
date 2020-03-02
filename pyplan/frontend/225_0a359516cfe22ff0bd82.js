/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[225,281],{1936:function(n,t,e){"use strict";(function(a,s){var o,i,l=e(18);o=[e(750),e(722),e(710),e(725),e(1937)],void 0===(i=function(n,t,o,i,c){return a.View.extend({el:s("#main"),_uId:"",groupPermissions:[],processLength:null,render:function(){s("div[data-rel='abm-permissions-group']").remove();var t,a,d=new n,r=this;this._uId=s.uuid();var p=this.options.companyId;t=new Promise(function(n,t){d.listPermissions(function(t){r.processLength=t.length,d.list(p,function(e){n({groupList:e,permissions:t})})})}),a=new Promise(function(n,t){e.e(23).then(function(){var t=[e(726)];(function(t){(new t).list(function(t){n(t.results)})}).apply(null,t)}).catch(e.oe)}),Promise.all([t,a]).then(function(n){var t=n[0].groupList,e=n[0].permissions,a=n[1],d={id:r._uId,dataRel:"abm-permissions-group",tmpClass:"rol-edit",title:(0,l.translate)("permissionsByGroup")},p={groups:r.prepareProcess(e),rolList:t,companyList:a,isSuper:__currentSession.userIsSuperUser},u=o(d),h=i(),m=c(p);r.$el.append(u),s("div[data-id='"+r._uId+"']").find("div.abm-content").append(h),s("div[data-id='"+r._uId+"']").find("div.form-content").append(m),s("div[data-id='"+r._uId+"']").find("form").removeClass("form-bordered"),s("div[data-id='"+r._uId+"']").find(".submit.form-actions").remove(),(0,l.postRender)(r.$el.find("div[data-id='"+r._uId+"']")),r.initCheckboxes(s("div[data-id='"+r._uId+"']"),t),r.addHandlers(s("div[data-id='"+r._uId+"']")),__currentSession.userIsSuperUser&&r.options.companyId&&s("div[data-id='"+r._uId+"']").find(".selCompany").select2("val",r.options.companyId)})},prepareProcess:function(n){for(var t,e=[],a={},s=0;s<n.length;s++){t=n[s],a[o];var o=t.content_type.model;a[o]?a[o].process.push(t):(a[o]={code:t.content_type.model,name:t.content_type.model,process:[]},a[o].process.push(t))}for(var i in a)e.push(a[i]);return e},save:function(){this.groupPermissions.length>0&&(new n).updateGroupPermissions(this.groupPermissions,function(){})},cancel:function(){Promise.resolve().then(function(){var n=[e(767)];(function(n){(new n).show()}).apply(null,n)}).catch(e.oe)},addHandlers:function(t){s("div[data-id='"+this._uId+"']").find("form").on("submit",s.proxy(function(){return this.save(),!1},this)),s("div[data-id='"+this._uId+"']").find("div.submit button.btn-cancel").on("click",s.proxy(function(){return this.cancel(),!1},this)),s("div[data-id='"+this._uId+"']").find("div.abm-top-options a.btn-close").on("click",this.cancel);var a=this;s("div[data-id='"+this._uId+"']").find(".selCompany").on("change",function(){var n=s(this).select2("val");Promise.resolve().then(function(){var t=[e(767)];(function(t){(new t).showPermisionsByGroup(n)}).apply(null,t)}).catch(e.oe)}),s("div[data-id='"+this._uId+"']").find("input[class!='chkAll'].permission").on("click",function(){var t=s(this).attr("data-rolId"),e=s(this).closest("tr").attr("data-processId");a.groupPermissions={group_id:t,permissions:[e]},(new n).updateGroupPermissions(a.groupPermissions,function(){a.groupPermissions={}})}),t.find("input[class='permission']").on("click",function(){var n=s(this).attr("data-groupcode"),t=s(this).attr("data-rolid");s("input[data-rolId='"+t+"'][data-groupcode='"+n+"'].permission:checked").length===s("input[data-rolId='"+t+"'][data-groupcode='"+n+"'].permission").length?s("input[class='chkAll'][data-groupcode='"+n+"'][data-rolId='"+t+"']").prop("checked",!0):s("input[class='chkAll'][data-groupcode='"+n+"'][data-rolId='"+t+"']").prop("checked",!1)}),t.find("input[class='chkAll']").on("click",function(){var e,o=s(this).prop("checked"),i=s(this).attr("data-rolId"),l=s(this).attr("data-groupCode");t.find("tbody input[class!='chkAll'][data-groupCode='"+l+"'][data-rolId='"+i+"']").each(function(n,t){o?s(this).prop("checked")||s(this).prop("checked","checked"):s(this).prop("checked")&&s(this).prop("checked","")}),a.groupPermissions={group_id:i,permissions:[],check_all:o},s.each(s("input[class!='chkAll'][data-groupcode='"+l+"'][data-rolId='"+i+"']"),function(n,t){e=s(t).closest("tr").attr("data-processId"),a.groupPermissions.permissions.push(e)}),(new n).updateGroupPermissions(a.groupPermissions,function(){a.groupPermissions={}})})},initCheckboxes:function(n,t){for(var e=0;e<t.length;e++){for(var a,o=t[e].id,i=0;i<t[e].permissions.length;i++){var l=t[e].permissions[i].codename;n.find("tr[data-processCode='"+l+"'] input[data-rolId='"+o+"']").prop("checked","checked")}for(i=0;i<t[e].permissions.length;i++)a=t[e].permissions[i].content_type.model,s("input[data-rolId='"+o+"'][data-groupcode='"+a+"'].permission:checked").length===s("input[data-rolId='"+o+"'][data-groupcode='"+a+"'].permission").length&&s("input[class='chkAll'][data-groupcode='"+a+"'][data-rolId='"+o+"']").prop("checked",!0)}}})}.apply(t,o))||(n.exports=i)}).call(this,e(218),e(1))},1937:function(n,t,e){var a=e(690);n.exports=(a.default||a).template({1:function(n,t,a,s,o){var i,l=null!=t?t:n.nullContext||{};return'<div class="row" style="margin-top: 15px; margin-bottom: 15px;">\n  <div class="col-sm-10">\n    <span style="float: left; padding-top: 5px; font-weight: bold;">'+n.escapeExpression(function(n){return n&&(n.__esModule?n.default:n)}(e(688)).call(l,"_company",{name:"L",hash:{},data:o}))+'</span>\n    <div class="col-sm-10">\n      <div class="col-sm-4">\n        <select class="select2-me selCompany" style="width: 100%;">\n'+(null!=(i=a.each.call(l,null!=t?t.companyList:t,{name:"each",hash:{},fn:n.program(2,o,0),inverse:n.noop,data:o}))?i:"")+"        </select>\n      </div>\n    </div>\n  </div>\n</div>\n"},2:function(n,t,e,a,s){var o=n.lambda,i=n.escapeExpression;return'          <option value="'+i(o(null!=t?t.id:t,t))+'">'+i(o(null!=t?t.name:t,t))+"</option>\n"},4:function(n,t,e,a,s,o,i){var l,c=n.lambda,d=n.escapeExpression,r=null!=t?t:n.nullContext||{};return'  <div class="panel panel-default">\n    <div class="panel-heading">\n      <h4 class="panel-title">\n        <a href="#'+d(c(null!=t?t.code:t,t))+'" data-toggle="collapse" data-parent="#ac4" class="collapsed">\n          '+d(c(null!=t?t.name:t,t))+'\n        </a>\n      </h4>\n      \x3c!-- /.panel-title --\x3e\n    </div>\n    \x3c!-- /.panel-heading --\x3e\n    <div id="'+d(c(null!=t?t.code:t,t))+'" class="panel-collapse collapse" style="height: 0px;">\n      <div class="panel-body">\n\n\n        <table class="table table-hover table-condensed processByRol">\n          <tbody>\n            <tr data-groupCode="'+d(c(null!=t?t.code:t,t))+'" class="group">\n              <td>\n                <strong></strong>\n              </td>\n'+(null!=(l=e.each.call(r,null!=i[1]?i[1].rolList:i[1],{name:"each",hash:{},fn:n.program(5,s,0,o,i),inverse:n.noop,data:s}))?l:"")+"            </tr>\n\n"+(null!=(l=e.each.call(r,null!=t?t.process:t,{name:"each",hash:{},fn:n.program(7,s,0,o,i),inverse:n.noop,data:s}))?l:"")+"          </tbody>\n        </table>\n\n\n      </div>\n      \x3c!-- /.panel-body --\x3e\n    </div>\n    \x3c!-- /#c1.panel-collapse collapse in --\x3e\n  </div>\n"},5:function(n,t,e,a,s,o,i){var l=n.lambda,c=n.escapeExpression;return'              <td class="group text-center">\n                '+c(l(null!=t?t.name:t,t))+' <br />\n\n                <label class="control centered control--checkbox">\n                  <input type="checkbox" class="chkAll" data-groupCode="'+c(l(null!=i[1]?i[1].code:i[1],t))+'" data-rolId="'+c(l(null!=t?t.id:t,t))+'" />\n                  <div class="control__indicator"></div>\n                </label>\n              </td>\n'},7:function(n,t,e,a,s,o,i){var l,c=n.lambda,d=n.escapeExpression;return'            <tr data-processCode="'+d(c(null!=t?t.codename:t,t))+'" data-processId="'+d(c(null!=t?t.id:t,t))+'" class="process">\n              <td style="width: 280px;"> ... '+d(c(null!=t?t.name:t,t))+"</td>\n"+(null!=(l=e.each.call(null!=t?t:n.nullContext||{},null!=i[2]?i[2].rolList:i[2],{name:"each",hash:{},fn:n.program(8,s,0,o,i),inverse:n.noop,data:s}))?l:"")+"            </tr>\n"},8:function(n,t,e,a,s,o,i){var l=n.lambda,c=n.escapeExpression;return'              <td class="process">\n                <label class="control nolabel control--checkbox">\n                  <input type="checkbox" class="permission" data-rolId="'+c(l(null!=t?t.id:t,t))+'" data-groupCode="'+c(l(null!=i[2]?i[2].code:i[2],t))+'" />\n                  <div class="control__indicator"></div>\n                </label>\n              </td>\n'},compiler:[7,">= 4.0.0"],main:function(n,t,e,a,s,o,i){var l,c=null!=t?t:n.nullContext||{};return(null!=(l=e.if.call(c,null!=t?t.isSuper:t,{name:"if",hash:{},fn:n.program(1,s,0,o,i),inverse:n.noop,data:s}))?l:"")+'<div class="panel-group novix-accordion">\n'+(null!=(l=e.each.call(c,null!=t?t.groups:t,{name:"each",hash:{},fn:n.program(4,s,0,o,i),inverse:n.noop,data:s}))?l:"")+"</div>"},useData:!0,useDepths:!0})},710:function(n,t,e){var a=e(690);n.exports=(a.default||a).template({compiler:[7,">= 4.0.0"],main:function(n,t,e,a,s){var o,i=null!=t?t:n.nullContext||{},l=e.helperMissing,c=n.escapeExpression;return'<div class="abm-base-tmp '+c("function"==typeof(o=null!=(o=e.tmpClass||(null!=t?t.tmpClass:t))?o:l)?o.call(i,{name:"tmpClass",hash:{},data:s}):o)+' container-fluid mainTask" data-id="'+c("function"==typeof(o=null!=(o=e.id||(null!=t?t.id:t))?o:l)?o.call(i,{name:"id",hash:{},data:s}):o)+'" data-rel="'+c("function"==typeof(o=null!=(o=e.dataRel||(null!=t?t.dataRel:t))?o:l)?o.call(i,{name:"dataRel",hash:{},data:s}):o)+'" data-type="tab-content">\n    <div class="row">\n        <div class="col-sm-12">\n            <div class="box">\n                <div class="box-title">\n                    <h3><i class="fa fa-th-list"></i>'+c("function"==typeof(o=null!=(o=e.title||(null!=t?t.title:t))?o:l)?o.call(i,{name:"title",hash:{},data:s}):o)+'</h3>\n                    <div class="actions abm-top-options">\n                        <a href="#" class="btn btn-close"><i class="fa fa-times"></i></a>\n                    </div>\n                </div>\n        <div class="box-content nopadding abm-content">\n\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n'},useData:!0})},725:function(n,t,e){var a=e(690);function s(n){return n&&(n.__esModule?n.default:n)}n.exports=(a.default||a).template({compiler:[7,">= 4.0.0"],main:function(n,t,a,o,i){var l=null!=t?t:n.nullContext||{},c=n.escapeExpression;return'<form action="#" id="baseForm" method="POST" class=\'form-horizontal form-bordered form-validate\' novalidate="novalidate">\n    <div class="form-content">\n\n    </div>\n    <div class="submit form-actions col-sm-12">\n        <button type="submit" class="btn btn-primary btn-save">'+c(s(e(688)).call(l,"_save",{name:"L",hash:{},data:i}))+'</button>\n        <button type="button" class="btn btn-cancel">'+c(s(e(688)).call(l,"cancel",{name:"L",hash:{},data:i}))+"</button>\n    </div>\n</form>\n"},useData:!0})},750:function(n,t,e){"use strict";(function(a){var s,o=e(693);void 0===(s=function(){return a.Model.extend({list:function(n,t){var e=null!=n?"?company_id=".concat(n):"";(0,o.send)("groups/".concat(e),null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},t)},get:function(n,t){(0,o.send)("groups/".concat(n,"/"),null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},t)},update:function(n,t,e){(0,o.send)("groups/".concat(n,"/"),JSON.stringify(t),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},e)},create:function(n,t){(0,o.send)("groups/",JSON.stringify(n),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},t)},delete:function(n,t){(0,o.send)("groups/".concat(n,"/"),null,{type:"DELETE"},t)},listPermissions:function(n){(0,o.send)("permissions/",null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n)},updateGroupPermissions:function(n,t){(0,o.send)("groups/update_groups_permissions/",JSON.stringify(n),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},t)}})}.apply(t,[]))||(n.exports=s)}).call(this,e(218))}}]);
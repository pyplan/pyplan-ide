/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[222,28],{1927:function(e,t,n){"use strict";(function(a,l){var s,i,r=n(18);s=[n(719),n(710),n(790),n(1928)],void 0===(i=function(e,t,s,i){return a.View.extend({el:l("#main"),_uId:"",render:function(){l("#mainLoading").show(),l("div[data-rel='abm-user']").remove();var n=new e,a=this;this._uId=l.uuid(),n.list(void 0,function(e){var n={id:a._uId,dataRel:"abm-user",tmpClass:"user-manager",title:(0,r.translate)("_userManager")},o={headers:[(0,r.translate)("_name"),(0,r.translate)("_login"),(0,r.translate)("_email"),(0,r.translate)("_companies"),(0,r.translate)("_options")]},d={data:e,token:__currentSession.token},c=t(n),u=s(o),p=i(d);a.$el.append(c),l("div[data-id='"+a._uId+"']").find("div.abm-content").append(u),l("div[data-id='"+a._uId+"']").find("tbody").append(p),(0,r.postRender)(a.$el.find("div[data-id='"+a._uId+"']")),a.addTableHandlers(l("div[data-id='"+a._uId+"']").find("table")),l("div[data-id='"+a._uId+"']").find("table").cubeTable(null,null,"userManagerSuper"),l("div[data-id='"+a._uId+"']").find("div.data-table-options").append(l('<a href="#" class="btn btn-adduser" rel="tooltip" data-title="'+(0,r.translate)("_newUser")+'"><i class="fa fa-plus"></i></a>')),a.addHandlers(),l("#mainLoading").hide()})},edit:function(e){var t=l(e.currentTarget).closest("tr").attr("data-id");Promise.resolve().then(function(){var e=[n(766)];(function(e){(new e).showEdit(t)}).apply(null,e)}).catch(n.oe)},editPreferences:function(e){var t=l(e.currentTarget).closest("tr").attr("data-id");Promise.resolve().then(function(){var e=[n(766)];(function(e){(new e).showEditPref(t)}).apply(null,e)}).catch(n.oe)},deleteUser:function(t){var a=l(t.currentTarget).closest("tr").attr("data-id");n.e(5).then(function(){var t=[n(683)];(function(t){(new t).show({title:(0,r.translate)("_deleteUser"),text:(0,r.translate)("_sure_delete_user"),buttons:[{title:(0,r.translate)("yes"),css:"primary",code:"yes"},{title:(0,r.translate)("no"),code:"no"}],callback:function(t){if("yes"==t){var s=new e;l("#mainLoading").show(),s.deleteUser(a,function(){l("#mainLoading").hide(),Promise.resolve().then(function(){var e=[n(766)];(function(e){(new e).show()}).apply(null,e)}).catch(n.oe)})}}})}).apply(null,t)}).catch(n.oe)},changeState:function(t){var n=l(this).closest("tr").attr("data-id"),a={user:{id:n,active:this.checked}};(new e).partialUpdate(n,a,function(){})},addUser:function(){Promise.resolve().then(function(){var e=[n(766)];(function(e){(new e).addUser()}).apply(null,e)}).catch(n.oe)},close:function(){var e=l("#currentTask").attr("data-rel");Promise.resolve().then(function(){var t=[n(684)];(function(t){(new t).removeTask(e)}).apply(null,t)}).catch(n.oe)},addTableHandlers:function(e){l(e).find("button.btn-edit").on("click",this.edit),l(e).find("button.btn-preference").on("click",this.editPreferences),l(e).find("input.user-state").on("ifToggled",this.changeState),l(e).find("button.btn-delete").on("click",this.deleteUser)},addHandlers:function(){l("div[data-id='"+this._uId+"']").find("div.data-table-options a.btn-adduser").on("click",this.addUser),l("div[data-id='"+this._uId+"']").find("div.abm-top-options a.btn-close").on("click",this.close),l(".iCheck-helper").attr("title",(0,r.translate)("_changeState")).tooltip()}})}.apply(t,s))||(e.exports=i)}).call(this,n(218),n(1))},1928:function(e,t,n){var a=n(690);function l(e){return e&&(e.__esModule?e.default:e)}e.exports=(a.default||a).template({1:function(e,t,a,s,i,r,o){var d,c=e.lambda,u=e.escapeExpression,p=null!=t?t:e.nullContext||{};return'<tr data-id="'+u(c(null!=t?t.id:t,t))+'">\n  <td class="userName">'+u(c(null!=t?t.first_name:t,t))+" "+u(c(null!=t?t.last_name:t,t))+"</td>\n  <td>"+u(c(null!=t?t.username:t,t))+"</td>\n  <td>"+u(c(null!=t?t.email:t,t))+"</td>\n  <td>\n"+(null!=(d=a.each.call(p,null!=t?t.companies:t,{name:"each",hash:{},fn:e.program(2,i,0,r,o),inverse:e.noop,data:i}))?d:"")+'  </td>\n  <td>\n    <div class="options">\n'+(null!=(d=l(n(695)).call(p,"impersonate_user",{name:"haveAccess",hash:{},fn:e.program(4,i,0,r,o),inverse:e.noop,data:i}))?d:"")+(null!=(d=l(n(695)).call(p,"change_user",{name:"haveAccess",hash:{},fn:e.program(6,i,0,r,o),inverse:e.noop,data:i}))?d:"")+'      \x3c!--button class="btn btn-mini btn-blue btn-preference" data-original-title=\''+u(l(n(688)).call(p,"_editUserPreferences",{name:"L",hash:{},data:i}))+"'\n        rel=\"tooltip\" data-title='"+u(l(n(688)).call(p,"_editUserPreferences",{name:"L",hash:{},data:i}))+'\'><i class="fa fa-list-ol"></i></button--\x3e\n'+(null!=(d=l(n(689)).call(p,null!=t?t.active:t,"==",!0,{name:"ifCond",hash:{},fn:e.program(8,i,0,r,o),inverse:e.program(10,i,0,r,o),data:i}))?d:"")+(null!=(d=l(n(695)).call(p,"delete_user",{name:"haveAccess",hash:{},fn:e.program(12,i,0,r,o),inverse:e.noop,data:i}))?d:"")+"    </div>\n  </td>\n</tr>\n"},2:function(e,t,n,a,l){return"    <li>"+e.escapeExpression(e.lambda(null!=t?t.name:t,t))+"</li>\n"},4:function(e,t,a,s,i,r,o){var d=e.lambda,c=e.escapeExpression,u=null!=t?t:e.nullContext||{};return'      <a class="btn btn-mini btn-darkblue" target="_blank" href="./#loginas/'+c(d(null!=o[1]?o[1].userId:o[1],t))+"/"+c(d(null!=o[2]?o[2].token:o[2],t))+"\"\n        data-original-title='"+c(l(n(688)).call(u,"login_as",{name:"L",hash:{},data:i}))+"' rel=\"tooltip\" data-title='"+c(l(n(688)).call(u,"login_as",{name:"L",hash:{},data:i}))+'\'><i\n          class="fa fa-external-link"></i></a>\n'},6:function(e,t,a,s,i){var r=null!=t?t:e.nullContext||{},o=e.escapeExpression;return'      <button class="btn btn-mini btn-green btn-edit" data-original-title=\''+o(l(n(688)).call(r,"_editUser",{name:"L",hash:{},data:i}))+"' rel=\"tooltip\"\n        data-title='"+o(l(n(688)).call(r,"_editUser",{name:"L",hash:{},data:i}))+'\'><i class="fa fa-pencil-square-o"></i></button>\n'},8:function(e,t,n,a,l){return'      <input type="checkbox" name="remember" class="icheck-me user-state" data-skin="square" data-color="blue" checked>\n'},10:function(e,t,n,a,l){return'      <input type="checkbox" name="remember" class="icheck-me user-state" data-skin="square" data-color="blue">\n'},12:function(e,t,a,s,i){var r=null!=t?t:e.nullContext||{},o=e.escapeExpression;return'      \x3c!--button class="btn btn-mini btn-red btn-delete" data-original-title=\''+o(l(n(688)).call(r,"_deleteUser",{name:"L",hash:{},data:i}))+"' rel=\"tooltip\"\n        data-title='"+o(l(n(688)).call(r,"_deleteUser",{name:"L",hash:{},data:i}))+'\'><i class="fa fa-trash"></i></button--\x3e\n'},compiler:[7,">= 4.0.0"],main:function(e,t,n,a,l,s,i){var r;return null!=(r=n.each.call(null!=t?t:e.nullContext||{},null!=t?t.data:t,{name:"each",hash:{},fn:e.program(1,l,0,s,i),inverse:e.noop,data:l}))?r:""},useData:!0,useDepths:!0})},710:function(e,t,n){var a=n(690);e.exports=(a.default||a).template({compiler:[7,">= 4.0.0"],main:function(e,t,n,a,l){var s,i=null!=t?t:e.nullContext||{},r=n.helperMissing,o=e.escapeExpression;return'<div class="abm-base-tmp '+o("function"==typeof(s=null!=(s=n.tmpClass||(null!=t?t.tmpClass:t))?s:r)?s.call(i,{name:"tmpClass",hash:{},data:l}):s)+' container-fluid mainTask" data-id="'+o("function"==typeof(s=null!=(s=n.id||(null!=t?t.id:t))?s:r)?s.call(i,{name:"id",hash:{},data:l}):s)+'" data-rel="'+o("function"==typeof(s=null!=(s=n.dataRel||(null!=t?t.dataRel:t))?s:r)?s.call(i,{name:"dataRel",hash:{},data:l}):s)+'" data-type="tab-content">\n    <div class="row">\n        <div class="col-sm-12">\n            <div class="box">\n                <div class="box-title">\n                    <h3><i class="fa fa-th-list"></i>'+o("function"==typeof(s=null!=(s=n.title||(null!=t?t.title:t))?s:r)?s.call(i,{name:"title",hash:{},data:l}):s)+'</h3>\n                    <div class="actions abm-top-options">\n                        <a href="#" class="btn btn-close"><i class="fa fa-times"></i></a>\n                    </div>\n                </div>\n        <div class="box-content nopadding abm-content">\n\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n'},useData:!0})},719:function(e,t,n){"use strict";(function(a){var l,s=n(693);void 0===(l=function(){return a.Model.extend({list:function(e,t){(0,s.send)("users/?page=1",null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},t)},listByCompany:function(e){(0,s.send)("usercompanies/list_by_company_id/",null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},e)},get:function(e,t){(0,s.send)("users/".concat(e,"/"),null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},t)},update:function(e,t,n){(0,s.send)("users/".concat(e,"/"),t,{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},n)},EditProfile:function(e,t){(0,s.send)("users/".concat(e.id,"/"),JSON.stringify(e),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},t)},create:function(e,t){(0,s.send)("usercompanies/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},t)},partialUpdate:function(e,t,n){(0,s.send)("usercompanies/".concat(e,"/"),JSON.stringify(t),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},n)},deleteUser:function(e,t){(0,s.send)("users/".concat(e,"/"),null,{type:"DELETE"},t)},deleteUserCompany:function(e,t){(0,s.send)("usercompanies/".concat(e,"/"),null,{type:"DELETE"},t)},UpdateUserPreference:function(e,t){var n={userCompanyId:__currentSession.userId,preferenceCode:e,value:t};(0,s.send)("user/UpdateUserPreference",n,{type:"PUT"})},GetUserPreference:function(e,t){(0,s.send)("usercompanies/preference_by_code/?code=".concat(e),null,{type:"GET"},t)},GetRelatedDashboard:function(e){(0,s.send)("user/GetRelatedDashboard",null,null,e)}})}.apply(t,[]))||(e.exports=l)}).call(this,n(218))},790:function(e,t,n){var a=n(690);e.exports=(a.default||a).template({1:function(e,t,n,a,l){return"      <th>"+e.escapeExpression(e.lambda(t,t))+"</th>\n"},compiler:[7,">= 4.0.0"],main:function(e,t,n,a,l){var s;return'<table class="table table-hover table-nomargin table-bordered">\n  <thead>\n    <tr>\n'+(null!=(s=n.each.call(null!=t?t:e.nullContext||{},null!=t?t.headers:t,{name:"each",hash:{},fn:e.program(1,l,0),inverse:e.noop,data:l}))?s:"")+"    </tr>\n  </thead>\n  <tbody>\n\n  </tbody>\n</table>"},useData:!0})}}]);
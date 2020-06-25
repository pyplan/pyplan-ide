/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[141],{2318:function(n,t,e){"use strict";(function(a,l){var o,i,r=e(18);o=[e(858),e(702),e(772),e(2319)],void 0===(i=function(n,t,o,i){return a.View.extend({el:l("#main"),_uId:"",render:function(){l("#mainLoading").show(),l("div[data-rel='abm-group']").remove();var e=new n,a=this;this._uId=l.uuid(),e.list(null,(function(n){var e={id:a._uId,dataRel:"abm-group",tmpClass:"group-manager",title:(0,r.translate)("_groupManager")},s={headers:[(0,r.translate)("_company"),(0,r.translate)("_name"),(0,r.translate)("_options")]};__currentSession.userIsSuperUser||s.headers.shift();var c={data:n,isSuper:__currentSession.userIsSuperUser},u=t(e),d=o(s),p=i(c);a.$el.append(u),l("div[data-id='"+a._uId+"']").find("div.abm-content").append(d),l("div[data-id='"+a._uId+"']").find("tbody").append(p),a.addTableHandlers(l("div[data-id='"+a._uId+"']").find("table")),l("div[data-id='"+a._uId+"']").find("table").cubeTable(null,null,"groupManagerSuper");var f=l("div[data-id='"+a._uId+"']").find("div.data-table-options");l('<a href="#" class="btn btn-addgroup" rel="tooltip" data-title="'+(0,r.translate)("_newGroup")+'"><i class="fa fa-plus"></i></a>').appendTo(f),a.addHandlers(),l("#mainLoading").hide()}))},edit:function(n){var t=l(n.currentTarget).closest("tr").attr("data-id");Promise.resolve().then((function(){var n=[e(800)];(function(n){(new n).showEdit(t)}).apply(null,n)})).catch(e.oe)},deleteGroup:function(t){var a=l(t.currentTarget).closest("tr").attr("data-id");e.e(6).then((function(){var t=[e(662)];(function(t){(new t).show({title:(0,r.translate)("_deleteGroup"),text:(0,r.translate)("_sure_delete_group"),buttons:[{title:(0,r.translate)("cancel"),code:"no"},{title:(0,r.translate)("delete"),css:"red",code:"yes"}],callback:function(t){if("yes"==t){var o=new n;l("#mainLoading").show(),o.delete(a,(function(){l("#mainLoading").hide(),Promise.resolve().then((function(){var n=[e(800)];(function(n){(new n).show()}).apply(null,n)})).catch(e.oe)}))}}})}).apply(null,t)})).catch(e.oe)},addGroup:function(){Promise.resolve().then((function(){var n=[e(800)];(function(n){(new n).addGroup()}).apply(null,n)})).catch(e.oe)},close:function(){var n=l("#currentTask").attr("data-rel");Promise.resolve().then((function(){var t=[e(663)];(function(t){(new t).removeTask(n)}).apply(null,t)})).catch(e.oe)},addTableHandlers:function(n){l(n).find("button.btn-edit").on("click",this.edit),l(n).find("button.btn-delete").on("click",this.deleteGroup)},addHandlers:function(){l("div[data-id='"+this._uId+"']").find("div.data-table-options a.btn-addgroup").on("click",this.addGroup),l("div[data-id='"+this._uId+"']").find("div.abm-top-options a.btn-close").on("click",this.close)}})}.apply(t,o))||(n.exports=i)}).call(this,e(219),e(1))},2319:function(n,t,e){var a=e(669);function l(n){return n&&(n.__esModule?n.default:n)}n.exports=(a.default||a).template({1:function(n,t,a,o,i,r,s){var c,u=n.lambda,d=n.escapeExpression,p=null!=t?t:n.nullContext||{},f=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return'<tr data-id="'+d(u(null!=t?f(t,"id"):t,t))+'">\n'+(null!=(c=f(a,"if").call(p,null!=s[1]?f(s[1],"isSuper"):s[1],{name:"if",hash:{},fn:n.program(2,i,0,r,s),inverse:n.noop,data:i,loc:{start:{line:3,column:8},end:{line:5,column:15}}}))?c:"")+'        <td class="groupName">'+d(u(null!=t?f(t,"name"):t,t))+"</td>\n        <td> "+(null!=(c=l(e(680)).call(p,"change_group",{name:"haveAccess",hash:{},fn:n.program(4,i,0,r,s),inverse:n.noop,data:i,loc:{start:{line:7,column:13},end:{line:10,column:31}}}))?c:"")+(null!=(c=l(e(680)).call(p,"delete_group",{name:"haveAccess",hash:{},fn:n.program(6,i,0,r,s),inverse:n.noop,data:i,loc:{start:{line:11,column:16},end:{line:14,column:31}}}))?c:"")+"        </td>\n</tr>\n"},2:function(n,t,e,a,l){var o,i=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return'        <td class="companyName">'+n.escapeExpression(n.lambda(null!=(o=null!=t?i(t,"company"):t)?i(o,"name"):o,t))+"</td>\n"},4:function(n,t,a,o,i){return'\n                <button class="btn btn-mini btn-green btn-edit" rel="tooltip" data-title=\''+n.escapeExpression(l(e(667)).call(null!=t?t:n.nullContext||{},"_editGroup",{name:"L",hash:{},data:i,loc:{start:{line:8,column:90},end:{line:8,column:108}}}))+'\'><i\n                                class="fa fa-pencil-square-o"></i></button>\n'},6:function(n,t,a,o,i){return'                \x3c!--button class="btn btn-mini btn-red btn-delete" rel="tooltip" data-title=\''+n.escapeExpression(l(e(667)).call(null!=t?t:n.nullContext||{},"_deleteGroup",{name:"L",hash:{},data:i,loc:{start:{line:12,column:93},end:{line:12,column:113}}}))+'\'><i\n                                class="fa fa-trash"></i></button--\x3e\n'},compiler:[8,">= 4.3.0"],main:function(n,t,e,a,l,o,i){var r,s=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return null!=(r=s(e,"each").call(null!=t?t:n.nullContext||{},null!=t?s(t,"data"):t,{name:"each",hash:{},fn:n.program(1,l,0,o,i),inverse:n.noop,data:l,loc:{start:{line:1,column:0},end:{line:17,column:9}}}))?r:""},useData:!0,useDepths:!0})},702:function(n,t,e){var a=e(669);n.exports=(a.default||a).template({compiler:[8,">= 4.3.0"],main:function(n,t,e,a,l){var o,i=null!=t?t:n.nullContext||{},r=n.hooks.helperMissing,s=n.escapeExpression,c=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return'<div class="abm-base-tmp '+s("function"==typeof(o=null!=(o=c(e,"tmpClass")||(null!=t?c(t,"tmpClass"):t))?o:r)?o.call(i,{name:"tmpClass",hash:{},data:l,loc:{start:{line:1,column:25},end:{line:1,column:37}}}):o)+' container-fluid mainTask" data-id="'+s("function"==typeof(o=null!=(o=c(e,"id")||(null!=t?c(t,"id"):t))?o:r)?o.call(i,{name:"id",hash:{},data:l,loc:{start:{line:1,column:73},end:{line:1,column:79}}}):o)+'" data-rel="'+s("function"==typeof(o=null!=(o=c(e,"dataRel")||(null!=t?c(t,"dataRel"):t))?o:r)?o.call(i,{name:"dataRel",hash:{},data:l,loc:{start:{line:1,column:91},end:{line:1,column:102}}}):o)+'" data-type="tab-content">\n    <div class="row">\n        <div class="col-sm-12">\n            <div class="box">\n                <div class="box-title">\n                    <h3><i class="fa fa-th-list"></i>'+s("function"==typeof(o=null!=(o=c(e,"title")||(null!=t?c(t,"title"):t))?o:r)?o.call(i,{name:"title",hash:{},data:l,loc:{start:{line:6,column:53},end:{line:6,column:62}}}):o)+'</h3>\n                    <div class="actions abm-top-options">\n                        <a href="#" class="btn btn-close"><i class="fa fa-times"></i></a>\n                    </div>\n                </div>\n        <div class="box-content nopadding abm-content">\n\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n'},useData:!0})},772:function(n,t,e){var a=e(669);n.exports=(a.default||a).template({1:function(n,t,e,a,l){return"      <th>"+n.escapeExpression(n.lambda(t,t))+"</th>\n"},compiler:[8,">= 4.3.0"],main:function(n,t,e,a,l){var o,i=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return'<table class="table table-hover table-nomargin table-bordered">\n  <thead>\n    <tr>\n'+(null!=(o=i(e,"each").call(null!=t?t:n.nullContext||{},null!=t?i(t,"headers"):t,{name:"each",hash:{},fn:n.program(1,l,0),inverse:n.noop,data:l,loc:{start:{line:4,column:6},end:{line:6,column:15}}}))?o:"")+"    </tr>\n  </thead>\n  <tbody>\n\n  </tbody>\n</table>"},useData:!0})},858:function(n,t,e){"use strict";(function(a){var l,o=e(678);void 0===(l=function(){return a.Model.extend({list:function(n,t){var e=null!=n?"?company_id=".concat(n):"";(0,o.send)("groups/".concat(e),null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},t)},get:function(n,t){(0,o.send)("groups/".concat(n,"/"),null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},t)},update:function(n,t,e){(0,o.send)("groups/".concat(n,"/"),JSON.stringify(t),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},e)},create:function(n,t){(0,o.send)("groups/",JSON.stringify(n),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},t)},delete:function(n,t){(0,o.send)("groups/".concat(n,"/"),null,{type:"DELETE"},t)},listPermissions:function(n){(0,o.send)("permissions/",null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n)},updateGroupPermissions:function(n,t){(0,o.send)("groups/update_groups_permissions/",JSON.stringify(n),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},t)}})}.apply(t,[]))||(n.exports=l)}).call(this,e(219))}}]);
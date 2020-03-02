/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[71],{1116:function(n,t,e){"use strict";(function(i){var a,d=e(693);void 0===(a=function(){return i.Model.extend({list:function(n){(0,d.send)("departments/?page=1",null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n)},getDepartment:function(n,t){(0,d.send)("departments/"+n+"/",null,null,t)},update:function(n,t,e){(0,d.send)("departments/"+n+"/",JSON.stringify(t),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},e)},partialUpdate:function(n,t,e){(0,d.send)("departments/"+n+"/",JSON.stringify(t),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},e)},create:function(n,t){(0,d.send)("departments/",JSON.stringify(n),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},t)},delete:function(n,t){(0,d.send)("departments/"+n+"/",null,{type:"DELETE"},t)}})}.apply(t,[]))||(n.exports=a)}).call(this,e(218))},1302:function(n,t,e){"use strict";(function(i,a){var d,o,l=e(18),s=function(n){return n&&n.__esModule?n:{default:n}}(e(1303));d=[e(1116),e(710),e(725),e(1919)],void 0===(o=function(n,t,d,o){return i.View.extend({el:a("#main"),_uId:"",definitionEditor:null,actionEditor:null,deniedEditor:null,render:function(){a("#mainLoading").show(),a("div[data-rel='abm-department']").remove();var i,r,c=new n,u=this;this._uId=a.uuid(),i=this.options.departmentId?new Promise(function(n,e){c.getDepartment(u.options.departmentId,function(e){var i={id:u._uId,dataRel:"abm-department",tmpClass:"department-edit",title:(0,l.translate)("_editDepartment")};e.engine_definitions=JSON.stringify(e.engine_definitions),e.login_action=JSON.stringify(e.login_action),e.denied_items=JSON.stringify(e.denied_items);var s={department:e,isSuper:__currentSession.userIsSuperUser},r=t(i),c=d(),p=o(s);u.$el.append(r),a("div[data-id='"+u._uId+"']").find("div.abm-content").append(c),a("div[data-id='"+u._uId+"']").find("div.form-content").append(p),n(e)})}):new Promise(function(n,e){var i={id:u._uId,dataRel:"abm-department",tmpClass:"department-create",title:(0,l.translate)("_newDepartment")},s={isSuper:__currentSession.userIsSuperUser},r=t(i),c=d(),p=o(s);u.$el.append(r),a("div[data-id='"+u._uId+"']").find("div.abm-content").append(c),a("div[data-id='"+u._uId+"']").find("div.form-content").append(p),a("div[data-id='"+u._uId+"']").find("div.department-code input").removeAttr("disabled"),n(null)}),r=new Promise(function(n,t){e.e(23).then(function(){var t=[e(726)];(function(t){(new t).list(function(t){n(t)})}).apply(null,t)}).catch(e.oe)}),Promise.all([i,r]).then(function(n){var t=n[1],e=a("div[data-id='"+u._uId+"'] div.company-id select");a.each(t.results,function(n,t){e.append(a("<option />").val(t.id).text(t.name))});var i=n[0],d=a("div[data-id='"+u._uId+"']").find(".engineDefinitions")[0],o={mode:"code",modes:["code","form","text","tree"]};u.definitionEditor=new s.default(d,o);var r=a("div[data-id='"+u._uId+"']").find(".loginAction")[0];o={mode:"code",modes:["code","form","text","tree"]};u.actionEditor=new s.default(r,o);var c=a("div[data-id='"+u._uId+"']").find(".deniedItems")[0];o={mode:"code",modes:["code","form","text","tree"]};(u.deniedEditor=new s.default(c,o),i)&&((e=a("div[data-id='"+u._uId+"'] div.company-id select")).val(i.company.id),""!==i.engine_definitions&&u.definitionEditor.set(JSON.parse(i.engine_definitions)),""!==i.login_action&&u.actionEditor.set(JSON.parse(i.login_action)),""!==i.denied_items&&u.deniedEditor.set(JSON.parse(i.denied_items)));(0,l.postRender)(u.$el.find("div[data-id='"+u._uId+"']")),u.addHandlers(),a("#mainLoading").hide()})},save:function(){var t=this._uId,i=a("div[data-id='"+t+"']").find("form");if(!a(i).validate().errorList.length>0){var d=a("div[data-id='"+t+"']").find("div.department-name input").val(),o=a("div[data-id='"+t+"']").find("div.department-code input").val(),l=a("div[data-id='"+t+"']").find("div.company-id select").val(),s=""===this.definitionEditor.get()?{}:this.definitionEditor.get(),r=""===this.actionEditor.get()?{}:this.actionEditor.get(),c=""===this.deniedEditor.get()?{}:this.deniedEditor.get(),u=new n,p={company_id:l,code:o,name:d,engine_definitions:""===a.trim(s)?"{}":JSON.stringify(s),login_action:""===a.trim(r)?"{}":JSON.stringify(r),denied_items:""===a.trim(c)?"{}":JSON.stringify(c)};__currentSession.userIsSuperUser&&(p.company_id=l),this.options.departmentId?u.partialUpdate(this.options.departmentId,p,function(){Promise.resolve().then(function(){var n=[e(807)];(function(n){(new n).show()}).apply(null,n)}).catch(e.oe)}):u.create(p,function(){Promise.resolve().then(function(){var n=[e(807)];(function(n){(new n).show()}).apply(null,n)}).catch(e.oe)})}},cancel:function(){Promise.resolve().then(function(){var n=[e(807)];(function(n){(new n).show()}).apply(null,n)}).catch(e.oe)},addHandlers:function(){a("div[data-id='"+this._uId+"']").find("form").on("submit",a.proxy(function(){return this.save(),!1},this)),a("div[data-id='"+this._uId+"']").find("div.submit button.btn-cancel").on("click",a.proxy(function(){return this.cancel(),!1},this)),a("div[data-id='"+this._uId+"']").find("div.abm-top-options a.btn-close").on("click",this.cancel)}})}.apply(t,d))||(n.exports=o)}).call(this,e(218),e(1))},1919:function(n,t,e){var i=e(690);function a(n){return n&&(n.__esModule?n.default:n)}n.exports=(i.default||i).template({1:function(n,t,i,d,o){return'<div class="form-group">\n    <label for="textfield" class="col-sm-2 control-label">'+n.escapeExpression(a(e(688)).call(null!=t?t:n.nullContext||{},"_company",{name:"L",hash:{},data:o}))+'</label>\n    <div class="col-sm-10">\n        <div class="col-sm-5 company-id">\n            <select class="form-control" data-rule-required="true">\n            </select>\n        </div>\n    </div>\n</div>\n'},compiler:[7,">= 4.0.0"],main:function(n,t,i,d,o){var l,s=null!=t?t:n.nullContext||{},r=n.escapeExpression,c=n.lambda;return'<div class="form-group">\n    <label for="textfield" class="col-sm-2 control-label">'+r(a(e(688)).call(s,"_name",{name:"L",hash:{},data:o}))+'</label>\n    <div class="col-sm-10">\n        <div class="col-sm-5 department-name">\n            <input type="text" value="'+r(c(null!=(l=null!=t?t.department:t)?l.name:l,t))+'" class="form-control" name="departmentName"\n                data-rule-required="true" data-rule-minlength="3">\n        </div>\n    </div>\n</div>\n<div class="form-group">\n    <label for="textfield" class=" col-sm-2 control-label">'+r(a(e(688)).call(s,"_code",{name:"L",hash:{},data:o}))+'</label>\n    <div class="col-sm-10">\n        <div class="col-sm-5 department-code">\n            <input type="text" value="'+r(c(null!=(l=null!=t?t.department:t)?l.code:l,t))+'" class="form-control" data-rule-required="true" disabled="disabled">\n        </div>\n    </div>\n</div>\n\n'+(null!=(l=a(e(689)).call(s,null!=t?t.isSuper:t,"==",!0,{name:"ifCond",hash:{},fn:n.program(1,o,0),inverse:n.noop,data:o}))?l:"")+'\n<div class="form-group">\n    <label for="textfield" class="col-sm-2 control-label">'+r(a(e(688)).call(s,"_engineDefinitions",{name:"L",hash:{},data:o}))+'</label>\n    <div class="col-sm-10 engineDefinitions">\n\n    </div>\n</div>\n<div class="form-group">\n    <label for="textfield" class="col-sm-2 control-label">'+r(a(e(688)).call(s,"_loginAction",{name:"L",hash:{},data:o}))+'</label>\n    <div class="col-sm-10 loginAction">\n    </div>\n</div>\n<div class="form-group">\n    <label for="textfield" class="col-sm-2 control-label">'+r(a(e(688)).call(s,"_deniedItems",{name:"L",hash:{},data:o}))+'</label>\n    <div class="col-sm-10 deniedItems">\n    </div>\n</div>'},useData:!0})},710:function(n,t,e){var i=e(690);n.exports=(i.default||i).template({compiler:[7,">= 4.0.0"],main:function(n,t,e,i,a){var d,o=null!=t?t:n.nullContext||{},l=e.helperMissing,s=n.escapeExpression;return'<div class="abm-base-tmp '+s("function"==typeof(d=null!=(d=e.tmpClass||(null!=t?t.tmpClass:t))?d:l)?d.call(o,{name:"tmpClass",hash:{},data:a}):d)+' container-fluid mainTask" data-id="'+s("function"==typeof(d=null!=(d=e.id||(null!=t?t.id:t))?d:l)?d.call(o,{name:"id",hash:{},data:a}):d)+'" data-rel="'+s("function"==typeof(d=null!=(d=e.dataRel||(null!=t?t.dataRel:t))?d:l)?d.call(o,{name:"dataRel",hash:{},data:a}):d)+'" data-type="tab-content">\n    <div class="row">\n        <div class="col-sm-12">\n            <div class="box">\n                <div class="box-title">\n                    <h3><i class="fa fa-th-list"></i>'+s("function"==typeof(d=null!=(d=e.title||(null!=t?t.title:t))?d:l)?d.call(o,{name:"title",hash:{},data:a}):d)+'</h3>\n                    <div class="actions abm-top-options">\n                        <a href="#" class="btn btn-close"><i class="fa fa-times"></i></a>\n                    </div>\n                </div>\n        <div class="box-content nopadding abm-content">\n\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n'},useData:!0})},725:function(n,t,e){var i=e(690);function a(n){return n&&(n.__esModule?n.default:n)}n.exports=(i.default||i).template({compiler:[7,">= 4.0.0"],main:function(n,t,i,d,o){var l=null!=t?t:n.nullContext||{},s=n.escapeExpression;return'<form action="#" id="baseForm" method="POST" class=\'form-horizontal form-bordered form-validate\' novalidate="novalidate">\n    <div class="form-content">\n\n    </div>\n    <div class="submit form-actions col-sm-12">\n        <button type="submit" class="btn btn-primary btn-save">'+s(a(e(688)).call(l,"_save",{name:"L",hash:{},data:o}))+'</button>\n        <button type="button" class="btn btn-cancel">'+s(a(e(688)).call(l,"cancel",{name:"L",hash:{},data:o}))+"</button>\n    </div>\n</form>\n"},useData:!0})}}]);
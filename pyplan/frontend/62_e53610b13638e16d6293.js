/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[62,26],{1585:function(n,e,a){"use strict";(function(t,o){var i,l,c=a(18);i=[a(721),a(703),a(751),a(2310)],void 0===(l=function(n,e,i,l){return t.View.extend({el:o("#main"),_uId:"",render:function(){var a=o("#mainLoading");a.show(),o('div[data-rel="abm-company"]').remove();var t=new n,s=this;if(this._uId=o.uuid(),this.options.companyId)t.getCompany(this.options.companyId,(function(n){var t={id:s._uId,dataRel:"abm-company",tmpClass:"company-edit",title:(0,c.translate)("_editCompany")},r={company:n},d=e(t),p=i(),m=l(r);s.$el.append(d);var u=o("div[data-id='".concat(s._uId,"']"));u.find("div.abm-content").append(p),u.find("div.form-content").append(m),(0,c.postRender)(u),s.addHandlers(),a.hide()}));else{var r={id:this._uId,dataRel:"abm-company",tmpClass:"company-create",title:(0,c.translate)("_newCompany")},d=e(r),p=i(),m=l();this.$el.append(d);var u=o("div[data-id='".concat(this._uId,"']"));u.find("div.abm-content").append(p),u.find("div.form-content").append(m),u.find("div.company-code input").removeAttr("disabled"),(0,c.postRender)(this.$el.find("div[data-id='"+this._uId+"']")),this.addHandlers(),a.hide()}},save:function(){var e=this._uId,t=o("div[data-id='".concat(e,"']")),i=t.find("form");if(!o(i).validate().errorList.length>0){var l=t.find("div.company-name input").val(),c=t.find("div.company-code input").val(),s=t.find("div.company-active input").is(":checked"),r=t.find("div.company-licence textarea").val(),d=o(".image_url").attr("src");"data:"!=d.substring(0,5)&&(d=this.imgToBase64("~img/logos/pyplan-only-logo-colors.png"));var p=new n,m={};this.options.companyId?(m={code:c,name:l,active:s,system:!1,image_url:d},""!=r.trim()&&(m.licence=r),p.partialUpdate(this.options.companyId,m,(function(){Promise.resolve().then((function(){var n=[a(764)];(function(n){(new n).show()}).apply(null,n)})).catch(a.oe)}))):(m={code:c,name:l,licence:r,active:s,image_url:d},p.create(m,(function(){Promise.resolve().then((function(){var n=[a(764)];(function(n){(new n).show()}).apply(null,n)})).catch(a.oe)})))}},cancel:function(){Promise.resolve().then((function(){var n=[a(764)];(function(n){(new n).show()}).apply(null,n)})).catch(a.oe)},addHandlers:function(){var n=this,e=o("div[data-id='".concat(this._uId,"']"));e.find("form").on("submit",(function(){return n.save(),!1})),e.find("div.submit button.btn-cancel").on("click",(function(){return n.cancel(),!1})),e.find("div.abm-top-options a.btn-close").on("click",this.cancel);var a=o(".companyName");o('input[name="companyname"]').keyup((function(){a.html(o(this).val())}));var t=o("#companyLogoUploader"),i=o("#fileElem"),l=o(".companyLogoErrorText"),c=function(n){n.preventDefault(),n.stopPropagation(),l[0].innerHTML=""},s=function(){t[0].classList.add("highlight")},r=function(){t[0].classList.remove("highlight")};t[0].addEventListener("dragenter",(function(n){c(n),s()}),!1),t[0].addEventListener("dragover",(function(n){c(n),s()}),!1),t[0].addEventListener("dragleave",(function(n){c(n),r()}),!1),t[0].addEventListener("drop",(function(e){c(e),r(),e.dataTransfer.files.length>0&&n.imgToBase64(e.dataTransfer.files[0])}),!1),i[0].addEventListener("change",(function(e){c(e),i[0].files.length>0&&n.imgToBase64(i[0].files[0])}),!1)},imgToBase64:function(n){if(["image/jpg","image/jpeg","image/png"].includes(n.type)){var e=o(".image_url"),a=n,t=new FileReader;t.onload=function(n){e.attr("src",n.target.result)},t.readAsDataURL(a)}else{o(".companyLogoErrorText")[0].innerHTML="Only .jpg, .jpeg or .png"}}})}.apply(e,i))||(n.exports=l)}).call(this,a(219),a(1))},2310:function(n,e,a){var t=a(670);function o(n){return n&&(n.__esModule?n.default:n)}n.exports=(t.default||t).template({1:function(n,e,a,t,o){return'    <input type="checkbox" class="icheck-me" value="1" data-skin="square" data-color="blue" checked />\n'},3:function(n,e,a,t,o){return'    <input type="checkbox" class="icheck-me" value="0" data-skin="square" data-color="blue" />\n'},5:function(n,e,a,t,o){var i,l=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'            <img class="image_url img-fluid" src='+n.escapeExpression(n.lambda(null!=(i=null!=e?l(e,"company"):e)?l(i,"image_url"):i,e))+" />\n"},7:function(n,e,a,t,o){return"            <img class=\"image_url img-fluid\" src='data:image/png;base64,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' />\n"},compiler:[8,">= 4.3.0"],main:function(n,e,t,i,l){var c,s=null!=e?e:n.nullContext||{},r=n.escapeExpression,d=n.lambda,p=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'<div class="form-group">\n  <label for="textfield" class="col-sm-2 control-label">'+r(o(a(668)).call(s,"_name",{name:"L",hash:{},data:l,loc:{start:{line:2,column:56},end:{line:2,column:69}}}))+'</label>\n  <div class="col-sm-10">\n    <div class="col-sm-6 company-name">\n      <input type="text" value="'+r(d(null!=(c=null!=e?p(e,"company"):e)?p(c,"name"):c,e))+'" class="form-control" name="companyname" data-rule-required="true"\n        data-rule-minlength="3" data-rule-maxlength="135">\n    </div>\n  </div>\n</div>\n<div class="form-group">\n  <label for="textfield" class=" col-sm-2 control-label">'+r(o(a(668)).call(s,"_code",{name:"L",hash:{},data:l,loc:{start:{line:11,column:57},end:{line:11,column:70}}}))+'</label>\n  <div class="col-sm-10">\n    <div class="col-sm-6 company-code">\n      <input type="text" value="'+r(d(null!=(c=null!=e?p(e,"company"):e)?p(c,"code"):c,e))+'" class="form-control" disabled="disabled" data-rule-required="true"\n        data-rule-maxlength="143">\n    </div>\n  </div>\n</div>\n<div class="form-group">\n  <label for="textfield" class="col-sm-2 control-label">'+r(o(a(668)).call(s,"active",{name:"L",hash:{},data:l,loc:{start:{line:20,column:56},end:{line:20,column:70}}}))+'</label>\n  <div class="col-sm-10 company-active">\n'+(null!=(c=o(a(669)).call(s,null!=(c=null!=e?p(e,"company"):e)?p(c,"active"):c,"==",!0,{name:"ifCond",hash:{},fn:n.program(1,l,0),inverse:n.program(3,l,0),data:l,loc:{start:{line:22,column:4},end:{line:26,column:15}}}))?c:"")+'  </div>\n</div>\n<div class="form-group">\n  <label for="textarea" class="col-sm-2 control-label">'+r(o(a(668)).call(s,"licence",{name:"L",hash:{},data:l,loc:{start:{line:30,column:55},end:{line:30,column:70}}}))+'</label>\n  <div class="company-licence col-sm-10">\n    <textarea rows="5" class="form-control">'+r(d(null!=(c=null!=e?p(e,"company"):e)?p(c,"licence"):c,e))+'</textarea>\n  </div>\n</div>\n\n<div class="row">\n  <div class="company-selector" style="align-items: flex-start; justify-content:flex-start">\n    <ul>\n      <li class="companyCard" style="width:200px;">\n        <div class="row nomargin" style="height:100%;">\n          <div class="companyLogo hidden-xs hidden-sm">\n'+(null!=(c=o(a(669)).call(s,null!=(c=null!=e?p(e,"company"):e)?p(c,"image_url"):c,"!=",null,{name:"ifCond",hash:{},fn:n.program(5,l,0),inverse:n.program(7,l,0),data:l,loc:{start:{line:42,column:12},end:{line:46,column:23}}}))?c:"")+'          </div>\n          <div class="companyName">\n            '+r(d(null!=(c=null!=e?p(e,"company"):e)?p(c,"name"):c,e))+'\n          </div>\n        </div>\n      </li>\n    </ul>\n  </div>\n</div>\n\n<div class="row">\n  <div id="companyLogoUploader">\n    <div class="row">\n      <p>Drag an Drop your company logo or</p>\n      <label class="lblUploadImage" for="fileElem">Click Here</label>\n      <input type="file" id="fileElem" accept=".jpg,.jpeg,.png">\n      <p class="companyLogoErrorText"></p>\n    </div>\n  </div>\n</div>'},useData:!0})},703:function(n,e,a){var t=a(670);n.exports=(t.default||t).template({compiler:[8,">= 4.3.0"],main:function(n,e,a,t,o){var i,l=null!=e?e:n.nullContext||{},c=n.hooks.helperMissing,s=n.escapeExpression,r=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'<div class="abm-base-tmp '+s("function"==typeof(i=null!=(i=r(a,"tmpClass")||(null!=e?r(e,"tmpClass"):e))?i:c)?i.call(l,{name:"tmpClass",hash:{},data:o,loc:{start:{line:1,column:25},end:{line:1,column:37}}}):i)+' container-fluid mainTask" data-id="'+s("function"==typeof(i=null!=(i=r(a,"id")||(null!=e?r(e,"id"):e))?i:c)?i.call(l,{name:"id",hash:{},data:o,loc:{start:{line:1,column:73},end:{line:1,column:79}}}):i)+'" data-rel="'+s("function"==typeof(i=null!=(i=r(a,"dataRel")||(null!=e?r(e,"dataRel"):e))?i:c)?i.call(l,{name:"dataRel",hash:{},data:o,loc:{start:{line:1,column:91},end:{line:1,column:102}}}):i)+'" data-type="tab-content">\n    <div class="row">\n        <div class="col-sm-12">\n            <div class="box">\n                <div class="box-title">\n                    <h3><i class="fa fa-th-list"></i>'+s("function"==typeof(i=null!=(i=r(a,"title")||(null!=e?r(e,"title"):e))?i:c)?i.call(l,{name:"title",hash:{},data:o,loc:{start:{line:6,column:53},end:{line:6,column:62}}}):i)+'</h3>\n                    <div class="actions abm-top-options">\n                        <a href="#" class="btn btn-close"><i class="fa fa-times"></i></a>\n                    </div>\n                </div>\n        <div class="box-content nopadding abm-content">\n\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n'},useData:!0})},721:function(n,e,a){"use strict";(function(t){var o,i=a(679);void 0===(o=function(){return t.Model.extend({list:function(n){(0,i.send)("companies/?limit=1000&offset=0",null,null,n)},getCompany:function(n,e){(0,i.send)("companies/".concat(n,"/"),null,null,e)},update:function(n,e,a){(0,i.send)("companies/".concat(n,"/"),JSON.stringify(e),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},a)},partialUpdate:function(n,e,a){(0,i.send)("companies/".concat(n,"/"),JSON.stringify(e),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},a)},create:function(n,e){(0,i.send)("companies/",n,{type:"POST"},e)},delete:function(n,e){(0,i.send)("companies/".concat(n,"/"),null,{type:"DELETE"},e)},preferences:function(n,e){(0,i.send)("companies/".concat(n,"/preferences/"),null,null,e)},saveCompanyPreference:function(n,e){var a=n.company,t=n.preference,o=n.definition;(0,i.send)("companyPreferences/",JSON.stringify({company:a,preference:t,definition:o}),{type:"POST",contentType:"application/json;charset=utf-8"},e)},updateCompanyPreference:function(n,e,a){var t=e.preference,o=e.definition;(0,i.send)("companyPreferences/".concat(n,"/"),JSON.stringify({id:n,preference:t,definition:o}),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},a)},removeCompanyPreference:function(n,e){(0,i.send)("companyPreferences/".concat(n,"/"),null,{type:"DELETE"},e)},GetCompanyPreference:function(n,e){(0,i.send)("companies/preference_by_code/?code=".concat(n),null,{type:"GET"},e)},sendTestEmail:function(n,e){(0,i.send)("company/SendTestEmail",n,{type:"PUT"},e)},getLicenceKey:function(n,e){(0,i.send)("company/GetLK/"+n,null,null,e)},setLicenceKey:function(n,e){(0,i.send)("company/SetLK/",n,{type:"POST"},e)}})}.apply(e,[]))||(n.exports=o)}).call(this,a(219))},751:function(n,e,a){var t=a(670);function o(n){return n&&(n.__esModule?n.default:n)}n.exports=(t.default||t).template({compiler:[8,">= 4.3.0"],main:function(n,e,t,i,l){var c=null!=e?e:n.nullContext||{},s=n.escapeExpression;return'<form action="#" id="baseForm" method="POST" class=\'form-horizontal form-bordered form-validate\' novalidate="novalidate">\n    <div class="form-content">\n\n    </div>\n    <div class="submit form-actions col-sm-12">\n        <button type="submit" class="btn btn-primary btn-save">'+s(o(a(668)).call(c,"_save",{name:"L",hash:{},data:l,loc:{start:{line:6,column:63},end:{line:6,column:76}}}))+'</button>\n        <button type="button" class="btn btn-cancel">'+s(o(a(668)).call(c,"cancel",{name:"L",hash:{},data:l,loc:{start:{line:7,column:53},end:{line:7,column:67}}}))+"</button>\n    </div>\n</form>\n"},useData:!0})}}]);
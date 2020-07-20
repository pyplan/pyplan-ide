/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[107,18,26,66,183],{1242:function(n,e,t){var o=t(670);function a(n){return n&&(n.__esModule?n.default:n)}n.exports=(o.default||o).template({1:function(n,e,o,i,s){var r,l=n.lambda,c=n.escapeExpression,u=null!=e?e:n.nullContext||{},d=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'<tr data-id="'+c(l(null!=e?d(e,"id"):e,e))+'">\n  <td>['+c(l(null!=(r=null!=e?d(e,"module"):e)?d(r,"description"):r,e))+"] "+c(l(null!=e?d(e,"description"):e,e))+"</td>\n  <td>"+c(l(null!=e?d(e,"definition"):e,e))+'</td>\n  <td>\n    <input type="text" value="'+c(l(null!=(r=null!=e?d(e,"custom"):e)?d(r,"definition"):r,e))+'" class="form-control" name="value" data-id="'+c(l(null!=(r=null!=e?d(e,"custom"):e)?d(r,"id"):r,e))+'" />\n  </td>\n  <td>\n'+(null!=(r=a(t(681)).call(u,"change_companypreference",{name:"haveAccess",hash:{},fn:n.program(2,s,0),inverse:n.noop,data:s,loc:{start:{line:9,column:4},end:{line:13,column:19}}}))?r:"")+(null!=(r=a(t(681)).call(u,"delete_companypreference",{name:"haveAccess",hash:{},fn:n.program(4,s,0),inverse:n.noop,data:s,loc:{start:{line:14,column:4},end:{line:18,column:19}}}))?r:"")+"  </td>\n</tr>\n"},2:function(n,e,o,i,s){return'    <button class="btn btn-mini btn-primary btn-save" rel="tooltip" data-title=\''+n.escapeExpression(a(t(668)).call(null!=e?e:n.nullContext||{},"_saveCustomValue",{name:"L",hash:{},data:s,loc:{start:{line:10,column:80},end:{line:10,column:104}}}))+'\'>\n      <i class="fal fa-save" />\n    </button>\n'},4:function(n,e,o,i,s){return'    <button class="btn btn-mini btn-red btn-remove" rel="tooltip" data-title=\''+n.escapeExpression(a(t(668)).call(null!=e?e:n.nullContext||{},"_removeCustomValue",{name:"L",hash:{},data:s,loc:{start:{line:15,column:78},end:{line:15,column:104}}}))+'\'>\n      <i class="fal fa-trash" />\n    </button>\n'},compiler:[8,">= 4.3.0"],main:function(n,e,t,o,a){var i,s=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return null!=(i=s(t,"each").call(null!=e?e:n.nullContext||{},null!=e?s(e,"data"):e,{name:"each",hash:{},fn:n.program(1,a,0),inverse:n.noop,data:a,loc:{start:{line:1,column:0},end:{line:21,column:9}}}))?i:""},useData:!0})},2314:function(n,e,t){"use strict";(function(o,a){var i,s,r=t(18);function l(n){for(var e=1;e<arguments.length;e++){var t=null!=arguments[e]?arguments[e]:{},o=Object.keys(t);"function"==typeof Object.getOwnPropertySymbols&&(o=o.concat(Object.getOwnPropertySymbols(t).filter((function(n){return Object.getOwnPropertyDescriptor(t,n).enumerable})))),o.forEach((function(e){c(n,e,t[e])}))}return n}function c(n,e,t){return e in n?Object.defineProperty(n,e,{value:t,enumerable:!0,configurable:!0,writable:!0}):n[e]=t,n}i=[t(665),t(721),t(703),t(773),t(1242)],void 0===(s=function(n,e,i,s,c){return o.View.extend({el:a("#main"),_uId:"",preferences:[],companyPreferences:[],render:function(){var n=this;this._uId=a.uuid();var t=a("#mainLoading");t.show(),a('div[data-rel="abm-company"]').remove(),(new e).preferences(this.options.companyId,(function(e){var o=e.preferences,u=e.companyPreferences;n.preferences=o,n.companyPreferences=u;var d={id:n._uId,dataRel:"abm-company",tmpClass:"company-pref-edit",title:"".concat((0,r.translate)("edit")," ").concat(n.options.companyName," ").concat((0,r.translate)("preferences").toLowerCase())},p=function(n){var e=u.find((function(e){return e.preference===n.id}));return e?l({},e,{definition:e.definition&&JSON.stringify(e.definition)}):null},f=o.map((function(n){return l({},n,{definition:n.definition&&JSON.stringify(n.definition),custom:p(n)})})),m={headers:[(0,r.translate)("_name"),(0,r.translate)("_default"),(0,r.translate)("_custom"),(0,r.translate)("_options")]},h=i(d),v=s(m),y=c({data:f});n.$el.append(h);var g=a("div[data-id='".concat(n._uId,"']"));g.find("div.abm-content").append(v),g.find("tbody").append(y),(0,r.postRender)(g),n.addHandlers(g),n.addTableHandlers(g.find("table")),t.hide()}))},save:function(t){var o=a(t.currentTarget.closest("tr")),i=o.children("td").find("input"),s=o.attr("data-id"),l=i.attr("data-id"),c=i.val(),u=new n;if((0,r.isValidJsonString)(c)){var d=JSON.parse(c),p=new e;l?p.updateCompanyPreference(parseInt(l),{preference:parseInt(s),definition:d},(function(){u.show({title:(0,r.translate)("_successfully_edited"),notifyType:"success"})})):p.saveCompanyPreference({company:this.options.companyId,preference:parseInt(s),definition:d},(function(n){i.attr("data-id",n.id),u.show({title:(0,r.translate)("_successfully_added"),notifyType:"success"})}))}else u.show({title:(0,r.translate)("saving_error"),text:(0,r.translate)("invalid_json_format")})},remove:function(t){var o=a(t.currentTarget.closest("tr")).children("td").find("input"),i=new n,s=o.attr("data-id");s?(new e).removeCompanyPreference(s,(function(){o.removeAttr("data-id"),o.val(null),i.show({title:(0,r.translate)("_successfully_removed"),notifyType:"success"})})):i.show({title:(0,r.translate)("nothing_to_delete"),notifyType:"info"})},cancel:function(){Promise.resolve().then((function(){var n=[t(764)];(function(n){(new n).show()}).apply(null,n)})).catch(t.oe)},addHandlers:function(n){n.find("div.abm-top-options a.btn-close").on("click",this.cancel)},addTableHandlers:function(n){var e=this;n.find("button.btn-save").on("click",(function(n){return e.save(n)})),n.find("button.btn-remove").on("click",(function(n){return e.remove(n)}))}})}.apply(e,i))||(n.exports=s)}).call(this,t(219),t(1))},665:function(n,e,t){"use strict";(function(o){var a,i,s=t(18);a=[t(761)],void 0===(i=function(n){return o.Controller.extend({name:"showNotify",currentProgressBar:void 0,show:function(e){var t=e.title,o=e.text,a=e.endpoint,i=e.notifyType,r=e.timeOut,l=e.tapToDismiss,c=e.buttons,u=e.showProgressBar,d=e.showFooter,p=e.callback,f=e.progressBar,m=void 0===f?null:f;if(m&&this.currentProgressBar&&this.currentProgressBar.length>0&&this.currentProgressBar.is(":visible"))return this.currentProgressBar.find(".toast-title").text(t),this.currentProgressBar.find(".toast-text").text(o),this.currentProgressBar.find(".progress-bar").css("width","".concat(m,"%")),void(m>=100&&(this.currentProgressBar.find(".progress").removeClass("active"),this.currentProgressBar.find('button[data-code="cancel"]').text((0,s.translate)("close")),this.currentProgressBar=void 0));var h=new n({title:t,text:o,endpoint:a,notifyType:i,timeOut:r,tapToDismiss:l,buttons:c,showProgressBar:u,showFooter:d,callback:p,progressBar:m}).render();m&&(this.currentProgressBar=h)}})}.apply(e,a))||(n.exports=i)}).call(this,t(677))},703:function(n,e,t){var o=t(670);n.exports=(o.default||o).template({compiler:[8,">= 4.3.0"],main:function(n,e,t,o,a){var i,s=null!=e?e:n.nullContext||{},r=n.hooks.helperMissing,l=n.escapeExpression,c=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'<div class="abm-base-tmp '+l("function"==typeof(i=null!=(i=c(t,"tmpClass")||(null!=e?c(e,"tmpClass"):e))?i:r)?i.call(s,{name:"tmpClass",hash:{},data:a,loc:{start:{line:1,column:25},end:{line:1,column:37}}}):i)+' container-fluid mainTask" data-id="'+l("function"==typeof(i=null!=(i=c(t,"id")||(null!=e?c(e,"id"):e))?i:r)?i.call(s,{name:"id",hash:{},data:a,loc:{start:{line:1,column:73},end:{line:1,column:79}}}):i)+'" data-rel="'+l("function"==typeof(i=null!=(i=c(t,"dataRel")||(null!=e?c(e,"dataRel"):e))?i:r)?i.call(s,{name:"dataRel",hash:{},data:a,loc:{start:{line:1,column:91},end:{line:1,column:102}}}):i)+'" data-type="tab-content">\n    <div class="row">\n        <div class="col-sm-12">\n            <div class="box">\n                <div class="box-title">\n                    <h3><i class="fa fa-th-list"></i>'+l("function"==typeof(i=null!=(i=c(t,"title")||(null!=e?c(e,"title"):e))?i:r)?i.call(s,{name:"title",hash:{},data:a,loc:{start:{line:6,column:53},end:{line:6,column:62}}}):i)+'</h3>\n                    <div class="actions abm-top-options">\n                        <a href="#" class="btn btn-close"><i class="fa fa-times"></i></a>\n                    </div>\n                </div>\n        <div class="box-content nopadding abm-content">\n\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n'},useData:!0})},721:function(n,e,t){"use strict";(function(o){var a,i=t(679);void 0===(a=function(){return o.Model.extend({list:function(n){(0,i.send)("companies/?limit=1000&offset=0",null,null,n)},getCompany:function(n,e){(0,i.send)("companies/".concat(n,"/"),null,null,e)},update:function(n,e,t){(0,i.send)("companies/".concat(n,"/"),JSON.stringify(e),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},t)},partialUpdate:function(n,e,t){(0,i.send)("companies/".concat(n,"/"),JSON.stringify(e),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},t)},create:function(n,e){(0,i.send)("companies/",n,{type:"POST"},e)},delete:function(n,e){(0,i.send)("companies/".concat(n,"/"),null,{type:"DELETE"},e)},preferences:function(n,e){(0,i.send)("companies/".concat(n,"/preferences/"),null,null,e)},saveCompanyPreference:function(n,e){var t=n.company,o=n.preference,a=n.definition;(0,i.send)("companyPreferences/",JSON.stringify({company:t,preference:o,definition:a}),{type:"POST",contentType:"application/json;charset=utf-8"},e)},updateCompanyPreference:function(n,e,t){var o=e.preference,a=e.definition;(0,i.send)("companyPreferences/".concat(n,"/"),JSON.stringify({id:n,preference:o,definition:a}),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},t)},removeCompanyPreference:function(n,e){(0,i.send)("companyPreferences/".concat(n,"/"),null,{type:"DELETE"},e)},GetCompanyPreference:function(n,e){(0,i.send)("companies/preference_by_code/?code=".concat(n),null,{type:"GET"},e)},sendTestEmail:function(n,e){(0,i.send)("company/SendTestEmail",n,{type:"PUT"},e)},getLicenceKey:function(n,e){(0,i.send)("company/GetLK/"+n,null,null,e)},setLicenceKey:function(n,e){(0,i.send)("company/SetLK/",n,{type:"POST"},e)}})}.apply(e,[]))||(n.exports=a)}).call(this,t(219))},737:function(n,e,t){var o,a;t(131),o=[t(1)],void 0===(a=function(n){return function(){function e(e,t){return e||(e=s()),(l=n("#"+e.containerId)).length||t&&(l=function(e){return(l=n("<div/>").attr("id",e.containerId).addClass(e.positionClass).attr("aria-live","polite").attr("role","alert")).appendTo(n(e.target)),l}(e)),l}function t(e){for(var t=l.children(),a=t.length-1;a>=0;a--)o(n(t[a]),e)}function o(e,t){return!(!e||0!==n(":focus",e).length||(e[t.hideMethod]({duration:t.hideDuration,easing:t.hideEasing,complete:function(){r(e)}}),0))}function a(n){c&&c(n)}function i(t){function o(e){return!n(":focus",f).length||e?(clearTimeout(g.intervalId),f[i.hideMethod]({duration:i.hideDuration,easing:i.hideEasing,complete:function(){r(f),i.onHidden&&"hidden"!==b.state&&i.onHidden(),b.state="hidden",b.endTime=new Date,a(b)}})):void 0}var i=s(),c=t.iconClass||i.iconClass;if(void 0!==t.optionsOverride&&(i=n.extend(i,t.optionsOverride),c=t.optionsOverride.iconClass||c),i.preventDuplicates){if(t.message===u)return;u=t.message}d++,l=e(i,!0);var p=null,f=n("<div/>"),m=n("<div/>"),h=n("<div/>"),v=n("<div/>"),y=n(i.closeHtml),g={intervalId:null,hideEta:null,maxHideTime:null},b={toastId:d,state:"visible",startTime:new Date,options:i,map:t};return t.iconClass&&f.addClass(i.toastClass).addClass(c),t.title&&(m.append(t.title).addClass(i.titleClass),f.append(m)),t.message&&(h.append(t.message).addClass(i.messageClass),f.append(h)),i.closeButton&&(y.addClass("toast-close-button").attr("role","button"),f.prepend(y)),i.progressBar&&(v.addClass("toast-progress"),f.prepend(v)),f.hide(),i.newestOnTop?l.prepend(f):l.append(f),f[i.showMethod]({duration:i.showDuration,easing:i.showEasing,complete:i.onShown}),i.timeOut>0&&(p=setTimeout(o,i.timeOut),g.maxHideTime=parseFloat(i.timeOut),g.hideEta=(new Date).getTime()+g.maxHideTime,i.progressBar&&(g.intervalId=setInterval((function(){var n=(g.hideEta-(new Date).getTime())/g.maxHideTime*100;v.width(n+"%")}),10))),f.hover((function(){clearTimeout(p),g.hideEta=0,f.stop(!0,!0)[i.showMethod]({duration:i.showDuration,easing:i.showEasing})}),(function(){(i.timeOut>0||i.extendedTimeOut>0)&&(p=setTimeout(o,i.extendedTimeOut),g.maxHideTime=parseFloat(i.extendedTimeOut),g.hideEta=(new Date).getTime()+g.maxHideTime)})),!i.onclick&&i.tapToDismiss&&f.click(o),i.closeButton&&y&&y.click((function(n){n.stopPropagation?n.stopPropagation():void 0!==n.cancelBubble&&!0!==n.cancelBubble&&(n.cancelBubble=!0),o(!0)})),i.onclick&&f.click((function(){i.onclick(),o()})),a(b),i.debug&&console&&console.log(b),f}function s(){return n.extend({},{tapToDismiss:!0,toastClass:"toast",containerId:"toast-container",debug:!1,showMethod:"fadeIn",showDuration:300,showEasing:"swing",onShown:void 0,hideMethod:"fadeOut",hideDuration:1e3,hideEasing:"swing",onHidden:void 0,extendedTimeOut:1e3,iconClasses:{error:"toast-error",info:"toast-info",success:"toast-success",warning:"toast-warning"},iconClass:"toast-info",positionClass:"toast-top-right",timeOut:5e3,titleClass:"toast-title",messageClass:"toast-message",target:"body",closeHtml:'<button type="button">&times;</button>',newestOnTop:!0,preventDuplicates:!1,progressBar:!1},f.options)}function r(n){l||(l=e()),n.is(":visible")||(n.remove(),n=null,0===l.children().length&&(l.remove(),u=void 0))}var l,c,u,d=0,p={error:"error",info:"info",success:"success",warning:"warning"},f={clear:function(n){var a=s();l||e(a),o(n,a)||t(a)},remove:function(t){var o=s();return l||e(o),t&&0===n(":focus",t).length?void r(t):void(l.children().length&&l.remove())},error:function(n,e,t){return i({type:p.error,iconClass:s().iconClasses.error,message:n,optionsOverride:t,title:e})},getContainer:e,info:function(n,e,t){return i({type:p.info,iconClass:s().iconClasses.info,message:n,optionsOverride:t,title:e})},options:{},subscribe:function(n){c=n},success:function(n,e,t){return i({type:p.success,iconClass:s().iconClasses.success,message:n,optionsOverride:t,title:e})},version:"2.1.0",warning:function(n,e,t){return i({type:p.warning,iconClass:s().iconClasses.warning,message:n,optionsOverride:t,title:e})}};return f}()}.apply(e,o))||(n.exports=a)},761:function(n,e,t){"use strict";(function(o,a){var i,s,r,l=(r=t(737))&&r.__esModule?r:{default:r},c=t(18);i=[t(762)],void 0===(s=function(n){return o.View.extend({el:a("#main"),currentProgressBar:void 0,defaults:{notifyType:"info",timeOut:3e3},initialize:function(){this.options=a.extend({},this.defaults,this.options)},render:function(){(this.options.buttons||this.options.progressBar)&&(this.options.showFooter=!0,this.options.progressBar&&(this.options.showProgressBar=!0)),l.default.options={closeButton:!0,closeHtml:'<button rel="tooltip" title="'.concat((0,c.translate)("close_all_notifications"),'" data-placement="left"><i class="fal fa-times"></i></button>'),debug:!1,newestOnTop:!1,progressBar:!1,positionClass:"toast-top-right",preventDuplicates:!1,onclick:null,showDuration:"300",hideDuration:"1000",timeOut:isNaN(parseInt(this.options.timeOut))?__currentSession.notificationTimeOut:this.options.timeOut,extendedTimeOut:0,showEasing:"swing",hideEasing:"linear",showMethod:"fadeIn",hideMethod:"fadeOut",tapToDismiss:this.options.tapToDismiss};var e=n(this.options),t=l.default[this.options.notifyType](e,this.options.title);(0,c.postRender)(t),this.options.notifyClass&&t.addClass(this.options.notifyClass);var o=this;return t.find(".footer-area button").click((function(){var n=!0;return o.options.callback&&!1===o.options.callback.call(this,a(this).attr("data-code"),t)&&(n=!1),n&&t.find(".toast-close-button").click(),!1})),t.find(".toast-close-button").click((function(n){n.preventDefault(),n.shiftKey&&a(".toast-close-button").click()})),t}})}.apply(e,i))||(n.exports=s)}).call(this,t(219),t(1))},762:function(n,e,t){var o=t(670);n.exports=(o.default||o).template({1:function(n,e,t,o,a){var i,s=null!=e?e:n.nullContext||{},r=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'<div class="footer-area">\n'+(null!=(i=r(t,"if").call(s,null!=e?r(e,"showProgressBar"):e,{name:"if",hash:{},fn:n.program(2,a,0),inverse:n.noop,data:a,loc:{start:{line:11,column:2},end:{line:15,column:9}}}))?i:"")+"\n"+(null!=(i=r(t,"each").call(s,null!=e?r(e,"buttons"):e,{name:"each",hash:{},fn:n.program(4,a,0),inverse:n.noop,data:a,loc:{start:{line:17,column:2},end:{line:19,column:11}}}))?i:"")+"\n</div>\n"},2:function(n,e,t,o,a){var i,s=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'  <div class="progress progress-striped active">\n    <div class="progress-bar progress-bar-warning" style="width: '+n.escapeExpression("function"==typeof(i=null!=(i=s(t,"progressBar")||(null!=e?s(e,"progressBar"):e))?i:n.hooks.helperMissing)?i.call(null!=e?e:n.nullContext||{},{name:"progressBar",hash:{},data:a,loc:{start:{line:13,column:65},end:{line:13,column:80}}}):i)+'%"></div>\n  </div>\n'},4:function(n,e,t,o,a){var i,s=null!=e?e:n.nullContext||{},r=n.hooks.helperMissing,l=n.escapeExpression,c=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'  <button class="btn btn-mini btn-'+l("function"==typeof(i=null!=(i=c(t,"css")||(null!=e?c(e,"css"):e))?i:r)?i.call(s,{name:"css",hash:{},data:a,loc:{start:{line:18,column:34},end:{line:18,column:41}}}):i)+'" data-code="'+l("function"==typeof(i=null!=(i=c(t,"code")||(null!=e?c(e,"code"):e))?i:r)?i.call(s,{name:"code",hash:{},data:a,loc:{start:{line:18,column:54},end:{line:18,column:62}}}):i)+'">'+l("function"==typeof(i=null!=(i=c(t,"title")||(null!=e?c(e,"title"):e))?i:r)?i.call(s,{name:"title",hash:{},data:a,loc:{start:{line:18,column:64},end:{line:18,column:73}}}):i)+"</button>\n"},compiler:[8,">= 4.3.0"],main:function(n,e,t,o,a){var i,s,r=null!=e?e:n.nullContext||{},l=n.hooks.helperMissing,c=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'<span class="toast-text">\n  <div>\n    '+(null!=(i="function"==typeof(s=null!=(s=c(t,"text")||(null!=e?c(e,"text"):e))?s:l)?s.call(r,{name:"text",hash:{},data:a,loc:{start:{line:3,column:4},end:{line:3,column:14}}}):s)?i:"")+"\n  </div>\n  <div>\n    "+(null!=(i="function"==typeof(s=null!=(s=c(t,"endpoint")||(null!=e?c(e,"endpoint"):e))?s:l)?s.call(r,{name:"endpoint",hash:{},data:a,loc:{start:{line:6,column:4},end:{line:6,column:18}}}):s)?i:"")+"\n  </div>\n</span>\n"+(null!=(i=c(t,"if").call(r,null!=e?c(e,"showFooter"):e,{name:"if",hash:{},fn:n.program(1,a,0),inverse:n.noop,data:a,loc:{start:{line:9,column:0},end:{line:22,column:7}}}))?i:"")},useData:!0})},773:function(n,e,t){var o=t(670);n.exports=(o.default||o).template({1:function(n,e,t,o,a){return"      <th>"+n.escapeExpression(n.lambda(e,e))+"</th>\n"},compiler:[8,">= 4.3.0"],main:function(n,e,t,o,a){var i,s=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'<table class="table table-hover table-nomargin table-bordered">\n  <thead>\n    <tr>\n'+(null!=(i=s(t,"each").call(null!=e?e:n.nullContext||{},null!=e?s(e,"headers"):e,{name:"each",hash:{},fn:n.program(1,a,0),inverse:n.noop,data:a,loc:{start:{line:4,column:6},end:{line:6,column:15}}}))?i:"")+"    </tr>\n  </thead>\n  <tbody>\n\n  </tbody>\n</table>"},useData:!0})}}]);
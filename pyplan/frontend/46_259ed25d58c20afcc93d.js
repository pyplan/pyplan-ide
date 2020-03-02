/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[46],{1063:function(t,e,n){var i=n(690);function s(t){return t&&(t.__esModule?t.default:t)}t.exports=(i.default||i).template({compiler:[7,">= 4.0.0"],main:function(t,e,i,o,a){var r=t.lambda,d=t.escapeExpression,l=null!=e?e:t.nullContext||{};return'<div class="print-report" data-key="'+d(r(null!=e?e.key:e,e))+'">\n    <span class="toast-text">'+d(r(null!=e?e.message:e,e))+'</span><br>\n\n    <div class="footer-area">\n\n        <div class="progress progress-striped active">\n            <div class="progress-bar progress-bar-warning" style="width: '+d(r(null!=e?e.percent:e,e))+'%"></div>\n        </div>\n\n        <a class="btn btn-small btn-blue btn--icon btnPrint" target="_blank" href="#" style="display:none" > <i class="fa fa-print"></i>'+d(s(n(688)).call(l,"print_report",{name:"L",hash:{},data:a}))+'</a>\n        <a class="btn btn-small btn-green btn--icon btnDownload" target="_blank" href="#" style="display:none"><i class="fa fa-download"></i>'+d(s(n(688)).call(l,"download",{name:"L",hash:{},data:a}))+'</a>\n\n        \x3c!--<button class="btn  btn-mini nodisplay" data-code="'+d(r(null!=e?e.code:e,e))+'">'+d(r(null!=e?e.title:e,e))+"</button>--\x3e\n    </div>\n</div>"},useData:!0})},739:function(t,e,n){"use strict";(function(i,s){var o,a,r=n(18),d=function(t){return t&&t.__esModule?t:{default:t}}(n(755));o=[n(1063)],void 0===(a=function(t){return i.View.extend({el:s("#main"),updatePrintReportProgress:function(){var e=this.options.key;if(0==s(".print-report[data-key='"+e+"']").length){var n=t(this.options);d.default.options={closeButton:!0,debug:!1,newestOnTop:!1,progressBar:!1,positionClass:"toast-top-right",preventDuplicates:!1,onclick:null,showDuration:"300",hideDuration:"1000",timeOut:-1,extendedTimeOut:0,showEasing:"swing",hideEasing:"linear",showMethod:"fadeIn",hideMethod:"fadeOut",tapToDismiss:!1};var i=d.default.info(n,(0,r.translate)("building")+" "+this.options.reportTitle);i.addClass("ademsg");var o=function(){i.find(".toast-close-button").click()};i.find(".btnPrint").on("click",o),i.find(".btnDownload").on("click",o)}var a=s(".print-report[data-key='"+e+"']");a.length>0&&(a.find(".progress-bar").css("width",this.options.percent+"%"),a.find(".toast-text").text(this.options.message))},updatePrintReportMessage:function(){var t=this.options.key,e=s(".print-report[data-key='"+t+"']");e.length>0&&(e.find(".toast-text").text((0,r.translate)(this.options.message)),e.find(".progress-bar").css("width","100%"))},updatePrintReportComplete:function(){var t=this.options.key,e=s(".print-report[data-key='"+t+"']");if(e.length>0){e.find(".toast-text").text((0,r.translate)("done")+"!"),e.find(".progress").hide(),e.find(".btnPrint").show(),e.find(".btnDownload").show();JSON.stringify([this.options.file]);e.find(".btnPrint").attr("href",""),e.find(".btnDownload").attr("href","")}}})}.apply(e,o))||(t.exports=a)}).call(this,n(218),n(1))},755:function(t,e,n){var i,s;n(135),i=[n(1)],void 0===(s=function(t){return function(){function e(e,n){return e||(e=a()),(d=t("#"+e.containerId)).length?d:(n&&(d=function(e){return(d=t("<div/>").attr("id",e.containerId).addClass(e.positionClass).attr("aria-live","polite").attr("role","alert")).appendTo(t(e.target)),d}(e)),d)}function n(e){for(var n=d.children(),s=n.length-1;s>=0;s--)i(t(n[s]),e)}function i(e,n){return!(!e||0!==t(":focus",e).length||(e[n.hideMethod]({duration:n.hideDuration,easing:n.hideEasing,complete:function(){r(e)}}),0))}function s(t){l&&l(t)}function o(n){function i(e){return!t(":focus",f).length||e?(clearTimeout(b.intervalId),f[o.hideMethod]({duration:o.hideDuration,easing:o.hideEasing,complete:function(){r(f),o.onHidden&&"hidden"!==w.state&&o.onHidden(),w.state="hidden",w.endTime=new Date,s(w)}})):void 0}var o=a(),l=n.iconClass||o.iconClass;if(void 0!==n.optionsOverride&&(o=t.extend(o,n.optionsOverride),l=n.optionsOverride.iconClass||l),o.preventDuplicates){if(n.message===c)return;c=n.message}u++,d=e(o,!0);var p=null,f=t("<div/>"),h=t("<div/>"),g=t("<div/>"),m=t("<div/>"),v=t(o.closeHtml),b={intervalId:null,hideEta:null,maxHideTime:null},w={toastId:u,state:"visible",startTime:new Date,options:o,map:n};return n.iconClass&&f.addClass(o.toastClass).addClass(l),n.title&&(h.append(n.title).addClass(o.titleClass),f.append(h)),n.message&&(g.append(n.message).addClass(o.messageClass),f.append(g)),o.closeButton&&(v.addClass("toast-close-button").attr("role","button"),f.prepend(v)),o.progressBar&&(m.addClass("toast-progress"),f.prepend(m)),f.hide(),o.newestOnTop?d.prepend(f):d.append(f),f[o.showMethod]({duration:o.showDuration,easing:o.showEasing,complete:o.onShown}),o.timeOut>0&&(p=setTimeout(i,o.timeOut),b.maxHideTime=parseFloat(o.timeOut),b.hideEta=(new Date).getTime()+b.maxHideTime,o.progressBar&&(b.intervalId=setInterval(function(){var t=(b.hideEta-(new Date).getTime())/b.maxHideTime*100;m.width(t+"%")},10))),f.hover(function(){clearTimeout(p),b.hideEta=0,f.stop(!0,!0)[o.showMethod]({duration:o.showDuration,easing:o.showEasing})},function(){(o.timeOut>0||o.extendedTimeOut>0)&&(p=setTimeout(i,o.extendedTimeOut),b.maxHideTime=parseFloat(o.extendedTimeOut),b.hideEta=(new Date).getTime()+b.maxHideTime)}),!o.onclick&&o.tapToDismiss&&f.click(i),o.closeButton&&v&&v.click(function(t){t.stopPropagation?t.stopPropagation():void 0!==t.cancelBubble&&!0!==t.cancelBubble&&(t.cancelBubble=!0),i(!0)}),o.onclick&&f.click(function(){o.onclick(),i()}),s(w),o.debug&&console&&console.log(w),f}function a(){return t.extend({},{tapToDismiss:!0,toastClass:"toast",containerId:"toast-container",debug:!1,showMethod:"fadeIn",showDuration:300,showEasing:"swing",onShown:void 0,hideMethod:"fadeOut",hideDuration:1e3,hideEasing:"swing",onHidden:void 0,extendedTimeOut:1e3,iconClasses:{error:"toast-error",info:"toast-info",success:"toast-success",warning:"toast-warning"},iconClass:"toast-info",positionClass:"toast-top-right",timeOut:5e3,titleClass:"toast-title",messageClass:"toast-message",target:"body",closeHtml:'<button type="button">&times;</button>',newestOnTop:!0,preventDuplicates:!1,progressBar:!1},f.options)}function r(t){d||(d=e()),t.is(":visible")||(t.remove(),t=null,0===d.children().length&&(d.remove(),c=void 0))}var d,l,c,u=0,p={error:"error",info:"info",success:"success",warning:"warning"},f={clear:function(t){var s=a();d||e(s),i(t,s)||n(s)},remove:function(n){var i=a();return d||e(i),n&&0===t(":focus",n).length?void r(n):void(d.children().length&&d.remove())},error:function(t,e,n){return o({type:p.error,iconClass:a().iconClasses.error,message:t,optionsOverride:n,title:e})},getContainer:e,info:function(t,e,n){return o({type:p.info,iconClass:a().iconClasses.info,message:t,optionsOverride:n,title:e})},options:{},subscribe:function(t){l=t},success:function(t,e,n){return o({type:p.success,iconClass:a().iconClasses.success,message:t,optionsOverride:n,title:e})},version:"2.1.0",warning:function(t,e,n){return o({type:p.warning,iconClass:a().iconClasses.warning,message:t,optionsOverride:n,title:e})}};return f}()}.apply(e,i))||(t.exports=s)}}]);
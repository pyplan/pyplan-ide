/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[199],{1131:function(t,n,e){"use strict";(function(s){var i,a=e(689);void 0===(i=function(){return s.Model.extend({sendPasswordResetEmail:function(t,n,e,s){(0,a.send)("sendPasswordResetEmail/",JSON.stringify({username:t,publicUrl:n}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},e,s)},passwordReset:function(t,n,e){(0,a.send)("passwordReset/",JSON.stringify({query:t}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},n,e)}})}.apply(n,[]))||(t.exports=i)}).call(this,e(220))},1714:function(t,n,e){"use strict";(function(s,i){var a,o;a=[e(1131),e(1715)],void 0===(o=function(t,n){return s.View.extend({el:i("#main"),render:function(t){var e=n();this.$el.append(e),this.addHandlers(t)},addHandlers:function(n){i("#appLoader").hide(),i("#resetPassword").on("click",(function(e){e.preventDefault(),i("#resetInfo").html(""),(new t).passwordReset(n.query,(function(t){i("#resetPassword").attr("disabled","disabled"),i("#resetInfo").html("An email has been sent to you with your new password")}),(function(t){i("#errorInfo").html(t)}))}))}})}.apply(n,a))||(t.exports=o)}).call(this,e(220),e(1))},1715:function(t,n,e){var s=e(681);t.exports=(s.default||s).template({compiler:[8,">= 4.3.0"],main:function(t,n,e,s,i){return'\n<div class="wrapper" style="width: 800px !important;\n  height: 300px !important;\n  position: absolute !important;\n  top: 50% !important;\n  left: 35% !important;\n  margin: -165px -150px !important;">\n    <div class="code" style="color: #fff !important;\n  font-size: 90px !important;\n  text-align: center !important;">\n        <i class="fa fa-warning"></i>\n        <span style="margin-right: 15px !important;">Reset Password</span>\t\t\n    </div>\n    <div class="desc" style="color: #fff !important;\n  font-size: 14px !important;\n  text-align: center;\n  margin: 20px 0 !important;">To reset your password please click the button.</div>\n  <div style="text-align: center;"><button class="btn btn-default" id="resetPassword">Reset Password</button></div>\t\n  <div style="text-align: center; color: white;" id="resetInfo"></div> \n  <div style="text-align: center; color: red;" id="errorInfo"></div> \n</div>\n    \n'},useData:!0})}}]);
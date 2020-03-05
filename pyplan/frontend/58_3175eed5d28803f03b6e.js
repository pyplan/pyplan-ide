/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[58,25],{722:function(n,e,t){"use strict";(function(o){var s,c=t(18),i=t(693);void 0===(s=function(){var n=function(n,e,o){null!==n.companySettingFile&&""!==n.companySettingFile&&t.e(39).then(function(){var e=[t(712)("./".concat(n.companySettingFile))];(function(){Promise.resolve().then(function(){t(221)}).catch(t.oe)}).apply(null,e)}).catch(t.oe),__currentSession=n,(0,c.setProcessDictionary)(n.process),(0,i.ajaxSetup)(),Promise.all([t.e(2),t.e(4),t.e(40)]).then(function(){var o=[t(684)];(function(t){(new t).clearUI(),e(n)}).apply(null,o)}).catch(t.oe)};return o.Model.extend({isConnected:function(){return""!=__currentToken&&null!==__currentSession},connect:function(n,e,t,o,s){var c={error:function(n,e,t){alert("Could not contact server ".concat(__apiURL))},type:"POST"};(0,i.send)("token-auth/",{username:n,password:e},c,function(n){n&&n.token&&(__currentToken=n.token,(0,i.ajaxSetup)(),o(n))},s,!0,!0)},createSession:function(e,t,o){(0,i.send)("security/createSession",{companyId:e,appVersion:__appVersion},{type:"POST"},function(e){n(e,t)},o)},getUserCompanies:function(n,e,t){(0,i.send)("security/getUserCompanies",{user:n,password:e},null,function(n){t(n)})},getUserCompaniesFromUserId:function(n,e){(0,i.send)("security/GetUserCompaniesFromUserId/?userId=".concat(n),null,null,function(n){e(n)})},logout:function(n){(0,i.send)("security/logout/",null,{dataType:"text"},function(e){void 0!=n&&n(e)})},getAllSessions:function(n){(0,i.send)("security/getAllSessions/",null,null,n,null,!0)},getMySessions:function(n){(0,i.send)("security/getMySessions/",null,null,n,null,!0)},getAllProcess:function(n){(0,i.send)("security/getAllProcess",null,null,n)},createFromToken:function(n,e,t){__currentToken=n,__currentSession={},(0,c.setProcessDictionary)([]),(0,i.ajaxSetup)(),(0,c.setLanguageDictionary)({}),e()},useExternalLink:function(n,e){(0,i.send)("security/useExternalLink/?guid=".concat(n),null,null,function(n,o){200===o.status?(null!==n.session.companySettingFile&&""!==n.session.companySettingFile&&t.e(39).then(function(){var e=[t(712)("./".concat(n.session.companySettingFile))];(function(){Promise.resolve().then(function(){t(221)}).catch(t.oe)}).apply(null,e)}).catch(t.oe),e(n,o)):e(n,o)})},killSessionByKey:function(n,e){(0,i.send)("security/killSessionByKey/",{session_key:n},{type:"GET",dataType:"text"},e)},createNewSession:function(e,t){(0,i.send)("security/createNewSession/",null,null,function(t){n(t,e)})},requireLogoutSessionByToken:function(n,e){(0,i.send)("security/requireLogout/",{session_key:n},{type:"GET",dataType:"text"},e)},ssoTest:function(){(0,i.send)("security/ssoTest",null,null,function(n){console.log(n)})},ssoCheckUser:function(n,e){(0,i.send)("security/SSOCheckUser/",null,null,n,e)},loginas:function(e,t,o,s,c){var u={error:function(n,e,t){alert("Could not contact server ".concat(__apiURL))}};(0,i.send)("security/loginas",{userId:e,token:t,companyId:o},u,function(e){n(e,s)})},loginFromToken:function(e,t,o){var s={error:function(n,e,t){alert("Could not contact server ".concat(__apiURL))}};(0,i.send)("security/loginFromToken",{token:e},s,function(e){n(e,t)})}})}.apply(e,[]))||(n.exports=s)}).call(this,t(218))}}]);
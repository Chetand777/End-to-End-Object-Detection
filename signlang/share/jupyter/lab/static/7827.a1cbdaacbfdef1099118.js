"use strict";(self["webpackChunk_jupyterlab_application_top"]=self["webpackChunk_jupyterlab_application_top"]||[]).push([[7827],{17827:(e,t,a)=>{a.r(t);a.d(t,{asterisk:()=>o});var n=["exten","same","include","ignorepat","switch"],i=["#include","#exec"],r=["addqueuemember","adsiprog","aelsub","agentlogin","agentmonitoroutgoing","agi","alarmreceiver","amd","answer","authenticate","background","backgrounddetect","bridge","busy","callcompletioncancel","callcompletionrequest","celgenuserevent","changemonitor","chanisavail","channelredirect","chanspy","clearhash","confbridge","congestion","continuewhile","controlplayback","dahdiacceptr2call","dahdibarge","dahdiras","dahdiscan","dahdisendcallreroutingfacility","dahdisendkeypadfacility","datetime","dbdel","dbdeltree","deadagi","dial","dictate","directory","disa","dumpchan","eagi","echo","endwhile","exec","execif","execiftime","exitwhile","extenspy","externalivr","festival","flash","followme","forkcdr","getcpeid","gosub","gosubif","goto","gotoif","gotoiftime","hangup","iax2provision","ices","importvar","incomplete","ivrdemo","jabberjoin","jabberleave","jabbersend","jabbersendgroup","jabberstatus","jack","log","macro","macroexclusive","macroexit","macroif","mailboxexists","meetme","meetmeadmin","meetmechanneladmin","meetmecount","milliwatt","minivmaccmess","minivmdelete","minivmgreet","minivmmwi","minivmnotify","minivmrecord","mixmonitor","monitor","morsecode","mp3player","mset","musiconhold","nbscat","nocdr","noop","odbc","odbc","odbcfinish","originate","ospauth","ospfinish","osplookup","ospnext","page","park","parkandannounce","parkedcall","pausemonitor","pausequeuemember","pickup","pickupchan","playback","playtones","privacymanager","proceeding","progress","queue","queuelog","raiseexception","read","readexten","readfile","receivefax","receivefax","receivefax","record","removequeuemember","resetcdr","retrydial","return","ringing","sayalpha","saycountedadj","saycountednoun","saycountpl","saydigits","saynumber","sayphonetic","sayunixtime","senddtmf","sendfax","sendfax","sendfax","sendimage","sendtext","sendurl","set","setamaflags","setcallerpres","setmusiconhold","sipaddheader","sipdtmfmode","sipremoveheader","skel","slastation","slatrunk","sms","softhangup","speechactivategrammar","speechbackground","speechcreate","speechdeactivategrammar","speechdestroy","speechloadgrammar","speechprocessingsound","speechstart","speechunloadgrammar","stackpop","startmusiconhold","stopmixmonitor","stopmonitor","stopmusiconhold","stopplaytones","system","testclient","testserver","transfer","tryexec","trysystem","unpausemonitor","unpausequeuemember","userevent","verbose","vmauthenticate","vmsayname","voicemail","voicemailmain","wait","waitexten","waitfornoise","waitforring","waitforsilence","waitmusiconhold","waituntil","while","zapateller"];function s(e,t){var a="";var r=e.next();if(t.blockComment){if(r=="-"&&e.match("-;",true)){t.blockComment=false}else if(e.skipTo("--;")){e.next();e.next();e.next();t.blockComment=false}else{e.skipToEnd()}return"comment"}if(r==";"){if(e.match("--",true)){if(!e.match("-",false)){t.blockComment=true;return"comment"}}e.skipToEnd();return"comment"}if(r=="["){e.skipTo("]");e.eat("]");return"header"}if(r=='"'){e.skipTo('"');return"string"}if(r=="'"){e.skipTo("'");return"string.special"}if(r=="#"){e.eatWhile(/\w/);a=e.current();if(i.indexOf(a)!==-1){e.skipToEnd();return"strong"}}if(r=="$"){var s=e.peek();if(s=="{"){e.skipTo("}");e.eat("}");return"variableName.special"}}e.eatWhile(/\w/);a=e.current();if(n.indexOf(a)!==-1){t.extenStart=true;switch(a){case"same":t.extenSame=true;break;case"include":case"switch":case"ignorepat":t.extenInclude=true;break;default:break}return"atom"}}const o={startState:function(){return{blockComment:false,extenStart:false,extenSame:false,extenInclude:false,extenExten:false,extenPriority:false,extenApplication:false}},token:function(e,t){var a="";if(e.eatSpace())return null;if(t.extenStart){e.eatWhile(/[^\s]/);a=e.current();if(/^=>?$/.test(a)){t.extenExten=true;t.extenStart=false;return"strong"}else{t.extenStart=false;e.skipToEnd();return"error"}}else if(t.extenExten){t.extenExten=false;t.extenPriority=true;e.eatWhile(/[^,]/);if(t.extenInclude){e.skipToEnd();t.extenPriority=false;t.extenInclude=false}if(t.extenSame){t.extenPriority=false;t.extenSame=false;t.extenApplication=true}return"tag"}else if(t.extenPriority){t.extenPriority=false;t.extenApplication=true;e.next();if(t.extenSame)return null;e.eatWhile(/[^,]/);return"number"}else if(t.extenApplication){e.eatWhile(/,/);a=e.current();if(a===",")return null;e.eatWhile(/\w/);a=e.current().toLowerCase();t.extenApplication=false;if(r.indexOf(a)!==-1){return"def"}}else{return s(e,t)}return null},languageData:{commentTokens:{line:";",block:{open:";--",close:"--;"}}}}}}]);
//# sourceMappingURL=7827.a1cbdaacbfdef1099118.js.map?v=a1cbdaacbfdef1099118
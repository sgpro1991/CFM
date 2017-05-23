

class TmpMail():
    '''
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    date = datetime.now().date()
    insert = Testimonials(name = name,date=date,text=message, switch=False)
    insert.save()
    '''

    def EMAIL_TEMPLATE_TESTIMONIALS(name,email,message):
        a = '''
        <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
       "http://www.w3.org/TR/html4/loose.dtd">

        <html lang="en">
        <head>
        	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        	<title>Писимо с сайта (отзыв)</title>
        	<style>
        	a:hover {
        		text-decoration: underline !important;
        	}
        	td.promocell p {
        		color:#e1d8c1;
        		font-size:16px;
        		line-height:26px;
        		font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
        		margin-top:0;
        		margin-bottom:0;
        		padding-top:0;
        		padding-bottom:14px;
        		font-weight:normal;
        	}
        	td.contentblock h4 {
        		color:#444444 !important;
        		font-size:16px;
        		line-height:24px;
        		font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
        		margin-top:0;
        		margin-bottom:10px;
        		padding-top:0;
        		padding-bottom:0;
        		font-weight:normal;
        	}
        	td.contentblock h4 a {
        		color:#444444;
        		text-decoration:none;
        	}
        	td.contentblock p {
        	  	color:#888888;
        		font-size:13px;
        		line-height:19px;
        		font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
        		margin-top:0;
        		margin-bottom:12px;
        		padding-top:0;
        		padding-bottom:0;
        		font-weight:normal;
        	}
        	td.contentblock p a {
        	  	color:#3ca7dd;
        		text-decoration:none;
        	}
        	@media only screen and (max-device-width: 480px) {
        	     div[class="header"] {
        	          font-size: 16px !important;
        	     }
        	     table[class="table"], td[class="cell"] {
        	          width: 300px !important;
        	     }
        		table[class="promotable"], td[class="promocell"] {
        	          width: 325px !important;
        	     }
        		td[class="footershow"] {
        	          width: 300px !important;
        	     }
        		table[class="hide"], img[class="hide"], td[class="hide"] {
        	          display: none !important;
        	     }
        	     img[class="divider"] {
        		      height: 1px !important;
        		 }
        		 td[class="logocell"] {
        			padding-top: 15px !important;
        			padding-left: 15px !important;
        			width: 300px !important;

        		 }
        	     img[id="screenshot"] {
        	          width: 325px !important;
        	          height: 127px !important;
        	     }
        		img[class="galleryimage"] {
        			  width: 53px !important;
        	          height: 53px !important;
        		}
        		p[class="reminder"] {
        			font-size: 11px !important;
        		}
        		h4[class="secondary"] {
        			line-height: 22px !important;
        			margin-bottom: 15px !important;
        			font-size: 18px !important;
        		}
        	}
        	</style>
        </head>
        <body bgcolor="#e4e4e4" topmargin="0" leftmargin="0" marginheight="0" marginwidth="0" style="-webkit-font-smoothing: antialiased;width:100% !important;background:#e4e4e4;-webkit-text-size-adjust:none;">

        <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#e4e4e4">
        <tr>
        	<td bgcolor="#e4e4e4" width="100%">

        	<table width="600" cellpadding="0" cellspacing="0" border="0" align="center" class="table">
        	<tr>
        		<td width="600" class="cell">

        	   	<table width="600" cellpadding="0" cellspacing="0" border="0" class="table">
        		<tr>
        			<td style="background:#fff;padding:10px;" width="250" bgcolor="#e4e4e4" class="logocell"><br class="hide"><img src="http://www.cfm.ru/img/logo.png" width="100" height="60" alt="Campaign Monitor" style="-ms-interpolation-mode:bicubic;"><br></td>

        		</tr>
        		</table>


        		<table width="600" cellpadding="25" cellspacing="0" border="0" class="promotable">
        		<tr>
        			<td bgcolor="#4db1e2" width="600" class="promocell">

        				<multiline label="Main feature intro"><p style="color:#fff">Письмо с сайта (отзыв)</p></multiline>

        			</td>
        		</tr>
        		</table>

        		<br>

        		<repeater>

        			<layout label="New feature">
        			<table width="100%" cellpadding="0" cellspacing="0" border="0">
        			<tr>
        				<td bgcolor="#85bdad" nowrap></td>
        				<td width="100%" bgcolor="#ffffff">

        					<table width="100%" cellpadding="20" cellspacing="0" border="0">
        					<tr>
        						<td bgcolor="#ffffff" class="contentblock">

        							<h4 class="secondary"><strong><singleline label="Title">Имя отправителя</singleline></strong></h4>
        							<multiline label="Description"><p>'''+name+'''</p></multiline>

        						</td>
        					</tr>
        					</table>

        				</td>
        			</tr>
        			</table>
        			<br>
        			</layout>

        			<layout label="Article, tip or resource">
        			<table width="100%" cellpadding="0" cellspacing="0" border="0">
        			<tr>
        				<td bgcolor="#ef3101" nowrap></td>
        				<td width="100%" bgcolor="#ffffff">

        					<table width="100%" cellpadding="20" cellspacing="0" border="0">
        					<tr>
        						<td bgcolor="#ffffff" class="contentblock">

        							<h4 class="secondary"><strong><singleline label="Title">Почта отправителя</singleline></strong></h4>
        							<multiline label="Description"><p>'''+email+'''</p></multiline>

        						</td>
        					</tr>
        					</table>

        				</td>
        			</tr>
        			</table>
        			<br>
        			</layout>

        			<layout label="Gallery highlights">
        			<table width="100%" cellpadding="0" cellspacing="0" border="0">
        			<tr>
        				<td bgcolor="#832701" nowrap></td>
        				<td width="100%" bgcolor="#ffffff">

        					<table width="100%" cellpadding="20" cellspacing="0" border="0">
        					<tr>
        						<td bgcolor="#ffffff" class="contentblock">

        							<h4 class="secondary"><strong><singleline label="Gallery title">Отзыв</singleline></strong></h4>
        							<multiline label="Gallery description"><p>'''+message+'''</p></multiline>

        						</td>
        					</tr>
        					</table>

        				</td>
        			</tr>
        			</table>

        			<table width="100%" cellpadding="0" cellspacing="0" border="0">

        			</table>
        <br>

        		</repeater>

        		</td>
        	</tr>
        	</table>

        	<img border="0" src="images/spacer.gif" width="1" height="25" class="divider"><br>

        	<table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f2f2f2">
        	<tr>
        		<td>

        	<br>

        			<table width="600" cellpadding="0" cellspacing="0" border="0" align="center" class="table">
        			<tr>
        				<td width="600" nowrap bgcolor="#f2f2f2" class="cell">

        					<table width="600" cellpadding="0" cellspacing="0" border="0" class="table">
        					<tr>
        						<td width="380" valign="top" class="footershow">

        							<br>

        							<p style="color:#a6a6a6;font-size:12px;font-family:Helvetica,Arial,sans-serif;margin-top:0;margin-bottom:15px;padding-top:0;padding-bottom:0;line-height:18px;" class="reminder">© «Центр семейной медицины», 2010-2014<br>
        Лицензия ЛО-66-01-003750 от 10.12.2015 <br><a href="http://www.cfm.ru/" style="color:#a6a6a6;text-decoration:underline;"> Перейти на сайт</a>.</p>

        						</td>
        						<td align="right" width="220" style="color:#a6a6a6;font-size:12px;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;text-shadow: 0 1px 0 #ffffff;" valign="top" class="hide">

        							<table cellpadding="0" cellspacing="0" border="0">
        							<tr>

        								<td><a href="https://vk.com/club76276932"><img border="0" src="http://www.cfm.ru/img/vk.png" width="32" height="32" alt="Follow us on Twitter"></a></td>

        							</tr>
        							</table>


        					</tr>
        					</table>

        				</td>
        			</tr>
        	   		</table>
        <br>

        	   </td>
        	</tr>
        	</table>

        	</td>
        </tr>
        </table>

        </body>
        </html>
        '''

        return a

    def EMAIL_TEMPLATE_FAQ(name,city,email,message):
            a = '''
            <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
           "http://www.w3.org/TR/html4/loose.dtd">

            <html lang="en">
            <head>
            	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            	<title>Писимо с сайта (отзыв)</title>
            	<style>
            	a:hover {
            		text-decoration: underline !important;
            	}
            	td.promocell p {
            		color:#e1d8c1;
            		font-size:16px;
            		line-height:26px;
            		font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
            		margin-top:0;
            		margin-bottom:0;
            		padding-top:0;
            		padding-bottom:14px;
            		font-weight:normal;
            	}
            	td.contentblock h4 {
            		color:#444444 !important;
            		font-size:16px;
            		line-height:24px;
            		font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
            		margin-top:0;
            		margin-bottom:10px;
            		padding-top:0;
            		padding-bottom:0;
            		font-weight:normal;
            	}
            	td.contentblock h4 a {
            		color:#444444;
            		text-decoration:none;
            	}
            	td.contentblock p {
            	  	color:#888888;
            		font-size:13px;
            		line-height:19px;
            		font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
            		margin-top:0;
            		margin-bottom:12px;
            		padding-top:0;
            		padding-bottom:0;
            		font-weight:normal;
            	}
            	td.contentblock p a {
            	  	color:#3ca7dd;
            		text-decoration:none;
            	}
            	@media only screen and (max-device-width: 480px) {
            	     div[class="header"] {
            	          font-size: 16px !important;
            	     }
            	     table[class="table"], td[class="cell"] {
            	          width: 300px !important;
            	     }
            		table[class="promotable"], td[class="promocell"] {
            	          width: 325px !important;
            	     }
            		td[class="footershow"] {
            	          width: 300px !important;
            	     }
            		table[class="hide"], img[class="hide"], td[class="hide"] {
            	          display: none !important;
            	     }
            	     img[class="divider"] {
            		      height: 1px !important;
            		 }
            		 td[class="logocell"] {
            			padding-top: 15px !important;
            			padding-left: 15px !important;
            			width: 300px !important;

            		 }
            	     img[id="screenshot"] {
            	          width: 325px !important;
            	          height: 127px !important;
            	     }
            		img[class="galleryimage"] {
            			  width: 53px !important;
            	          height: 53px !important;
            		}
            		p[class="reminder"] {
            			font-size: 11px !important;
            		}
            		h4[class="secondary"] {
            			line-height: 22px !important;
            			margin-bottom: 15px !important;
            			font-size: 18px !important;
            		}
            	}
            	</style>
            </head>
            <body bgcolor="#e4e4e4" topmargin="0" leftmargin="0" marginheight="0" marginwidth="0" style="-webkit-font-smoothing: antialiased;width:100% !important;background:#e4e4e4;-webkit-text-size-adjust:none;">

            <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#e4e4e4">
            <tr>
            	<td bgcolor="#e4e4e4" width="100%">

            	<table width="600" cellpadding="0" cellspacing="0" border="0" align="center" class="table">
            	<tr>
            		<td width="600" class="cell">

            	   	<table width="600" cellpadding="0" cellspacing="0" border="0" class="table">
            		<tr>
            			<td style="background:#fff;padding:10px;" width="250" bgcolor="#e4e4e4" class="logocell"><br class="hide"><img src="http://www.cfm.ru/img/logo.png" width="100" height="60" alt="Campaign Monitor" style="-ms-interpolation-mode:bicubic;"><br></td>

            		</tr>
            		</table>


            		<table width="600" cellpadding="25" cellspacing="0" border="0" class="promotable">
            		<tr>
            			<td bgcolor="#4db1e2" width="600" class="promocell">

            				<multiline label="Main feature intro"><p style="color:#fff">Письмо с сайта (Вопрос)</p></multiline>

            			</td>
            		</tr>
            		</table>

            		<br>

            		<repeater>

            			<layout label="New feature">
            			<table width="100%" cellpadding="0" cellspacing="0" border="0">
            			<tr>
            				<td bgcolor="#85bdad" nowrap></td>
            				<td width="100%" bgcolor="#ffffff">

            					<table width="100%" cellpadding="20" cellspacing="0" border="0">
            					<tr>
            						<td bgcolor="#ffffff" class="contentblock">

            							<h4 class="secondary"><strong><singleline label="Title">Имя отправителя</singleline></strong></h4>
            							<multiline label="Description"><p>'''+name+'''</p></multiline>

            						</td>
            					</tr>
            					</table>

            				</td>
            			</tr>
            			</table>
            			<br>
            			</layout>

            			<layout label="New feature">
            			<table width="100%" cellpadding="0" cellspacing="0" border="0">
            			<tr>
            				<td bgcolor="#85bdad" nowrap></td>
            				<td width="100%" bgcolor="#ffffff">

            					<table width="100%" cellpadding="20" cellspacing="0" border="0">
            					<tr>
            						<td bgcolor="#ffffff" class="contentblock">

            							<h4 class="secondary"><strong><singleline label="Title">Город</singleline></strong></h4>
            							<multiline label="Description"><p>'''+city+'''</p></multiline>

            						</td>
            					</tr>
            					</table>

            				</td>
            			</tr>
            			</table>
            			<br>
            			</layout>

            			<layout label="Article, tip or resource">
            			<table width="100%" cellpadding="0" cellspacing="0" border="0">
            			<tr>
            				<td bgcolor="#ef3101" nowrap></td>
            				<td width="100%" bgcolor="#ffffff">

            					<table width="100%" cellpadding="20" cellspacing="0" border="0">
            					<tr>
            						<td bgcolor="#ffffff" class="contentblock">

            							<h4 class="secondary"><strong><singleline label="Title">Почта отправителя</singleline></strong></h4>
            							<multiline label="Description"><p>'''+email+'''</p></multiline>

            						</td>
            					</tr>
            					</table>

            				</td>
            			</tr>
            			</table>
            			<br>
            			</layout>

            			<layout label="Gallery highlights">
            			<table width="100%" cellpadding="0" cellspacing="0" border="0">
            			<tr>
            				<td bgcolor="#832701" nowrap></td>
            				<td width="100%" bgcolor="#ffffff">

            					<table width="100%" cellpadding="20" cellspacing="0" border="0">
            					<tr>
            						<td bgcolor="#ffffff" class="contentblock">

            							<h4 class="secondary"><strong><singleline label="Gallery title">Вопрос</singleline></strong></h4>
            							<multiline label="Gallery description"><p>'''+message+'''</p></multiline>

            						</td>
            					</tr>
            					</table>

            				</td>
            			</tr>
            			</table>

            			<table width="100%" cellpadding="0" cellspacing="0" border="0">

            			</table>
            <br>

            		</repeater>

            		</td>
            	</tr>
            	</table>

            	<img border="0" src="images/spacer.gif" width="1" height="25" class="divider"><br>

            	<table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f2f2f2">
            	<tr>
            		<td>

            	<br>

            			<table width="600" cellpadding="0" cellspacing="0" border="0" align="center" class="table">
            			<tr>
            				<td width="600" nowrap bgcolor="#f2f2f2" class="cell">

            					<table width="600" cellpadding="0" cellspacing="0" border="0" class="table">
            					<tr>
            						<td width="380" valign="top" class="footershow">

            							<br>

            							<p style="color:#a6a6a6;font-size:12px;font-family:Helvetica,Arial,sans-serif;margin-top:0;margin-bottom:15px;padding-top:0;padding-bottom:0;line-height:18px;" class="reminder">© «Центр семейной медицины», 2010-2014<br>
            Лицензия ЛО-66-01-003750 от 10.12.2015 <br><a href="http://www.cfm.ru/" style="color:#a6a6a6;text-decoration:underline;"> Перейти на сайт</a>.</p>

            						</td>
            						<td align="right" width="220" style="color:#a6a6a6;font-size:12px;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;text-shadow: 0 1px 0 #ffffff;" valign="top" class="hide">

            							<table cellpadding="0" cellspacing="0" border="0">
            							<tr>

            								<td><a href="https://vk.com/club76276932"><img border="0" src="http://www.cfm.ru/img/vk.png" width="32" height="32" alt="Follow us on Twitter"></a></td>

            							</tr>
            							</table>


            					</tr>
            					</table>

            				</td>
            			</tr>
            	   		</table>
            <br>

            	   </td>
            	</tr>
            	</table>

            	</td>
            </tr>
            </table>

            </body>
            </html>
            '''

            return a

    def EMAIL_TEMPLATE_ONLINE(name,post,message,phone,date,priem):
                    a = '''
                    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
                   "http://www.w3.org/TR/html4/loose.dtd">

                    <html lang="en">
                    <head>
                    	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                    	<title>Писимо с сайта (отзыв)</title>
                    	<style>
                    	a:hover {
                    		text-decoration: underline !important;
                    	}
                    	td.promocell p {
                    		color:#e1d8c1;
                    		font-size:16px;
                    		line-height:26px;
                    		font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
                    		margin-top:0;
                    		margin-bottom:0;
                    		padding-top:0;
                    		padding-bottom:14px;
                    		font-weight:normal;
                    	}
                    	td.contentblock h4 {
                    		color:#444444 !important;
                    		font-size:16px;
                    		line-height:24px;
                    		font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
                    		margin-top:0;
                    		margin-bottom:10px;
                    		padding-top:0;
                    		padding-bottom:0;
                    		font-weight:normal;
                    	}
                    	td.contentblock h4 a {
                    		color:#444444;
                    		text-decoration:none;
                    	}
                    	td.contentblock p {
                    	  	color:#888888;
                    		font-size:13px;
                    		line-height:19px;
                    		font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
                    		margin-top:0;
                    		margin-bottom:12px;
                    		padding-top:0;
                    		padding-bottom:0;
                    		font-weight:normal;
                    	}
                    	td.contentblock p a {
                    	  	color:#3ca7dd;
                    		text-decoration:none;
                    	}
                    	@media only screen and (max-device-width: 480px) {
                    	     div[class="header"] {
                    	          font-size: 16px !important;
                    	     }
                    	     table[class="table"], td[class="cell"] {
                    	          width: 300px !important;
                    	     }
                    		table[class="promotable"], td[class="promocell"] {
                    	          width: 325px !important;
                    	     }
                    		td[class="footershow"] {
                    	          width: 300px !important;
                    	     }
                    		table[class="hide"], img[class="hide"], td[class="hide"] {
                    	          display: none !important;
                    	     }
                    	     img[class="divider"] {
                    		      height: 1px !important;
                    		 }
                    		 td[class="logocell"] {
                    			padding-top: 15px !important;
                    			padding-left: 15px !important;
                    			width: 300px !important;

                    		 }
                    	     img[id="screenshot"] {
                    	          width: 325px !important;
                    	          height: 127px !important;
                    	     }
                    		img[class="galleryimage"] {
                    			  width: 53px !important;
                    	          height: 53px !important;
                    		}
                    		p[class="reminder"] {
                    			font-size: 11px !important;
                    		}
                    		h4[class="secondary"] {
                    			line-height: 22px !important;
                    			margin-bottom: 15px !important;
                    			font-size: 18px !important;
                    		}
                    	}
                    	</style>
                    </head>
                    <body bgcolor="#e4e4e4" topmargin="0" leftmargin="0" marginheight="0" marginwidth="0" style="-webkit-font-smoothing: antialiased;width:100% !important;background:#e4e4e4;-webkit-text-size-adjust:none;">

                    <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#e4e4e4">
                    <tr>
                    	<td bgcolor="#e4e4e4" width="100%">

                    	<table width="600" cellpadding="0" cellspacing="0" border="0" align="center" class="table">
                    	<tr>
                    		<td width="600" class="cell">

                    	   	<table width="600" cellpadding="0" cellspacing="0" border="0" class="table">
                    		<tr>
                    			<td style="background:#fff;padding:10px;" width="250" bgcolor="#e4e4e4" class="logocell"><br class="hide"><img src="http://www.cfm.ru/img/logo.png" width="100" height="60" alt="Campaign Monitor" style="-ms-interpolation-mode:bicubic;"><br></td>

                    		</tr>
                    		</table>


                    		<table width="600" cellpadding="25" cellspacing="0" border="0" class="promotable">
                    		<tr>
                    			<td bgcolor="#4db1e2" width="600" class="promocell">

                    				<multiline label="Main feature intro"><p style="color:#fff">Письмо с сайта (Онлай запись)</p></multiline>

                    			</td>
                    		</tr>
                    		</table>

                    		<br>

                    		<repeater>

                    			<layout label="New feature">
                    			<table width="100%" cellpadding="0" cellspacing="0" border="0">
                    			<tr>
                    				<td bgcolor="#85bdad" nowrap></td>
                    				<td width="100%" bgcolor="#ffffff">

                    					<table width="100%" cellpadding="20" cellspacing="0" border="0">
                    					<tr>
                    						<td bgcolor="#ffffff" class="contentblock">

                    							<h4 class="secondary"><strong><singleline label="Title">Имя отправителя</singleline></strong></h4>
                    							<multiline label="Description"><p>'''+name+'''</p></multiline>

                    						</td>
                    					</tr>
                    					</table>

                    				</td>
                    			</tr>
                    			</table>
                    			<br>
                    			</layout>

                    			<layout label="New feature">
                    			<table width="100%" cellpadding="0" cellspacing="0" border="0">
                    			<tr>
                    				<td bgcolor="#85bdad" nowrap></td>
                    				<td width="100%" bgcolor="#ffffff">

                    					<table width="100%" cellpadding="20" cellspacing="0" border="0">
                    					<tr>
                    						<td bgcolor="#ffffff" class="contentblock">

                    							<h4 class="secondary"><strong><singleline label="Title">Телефон</singleline></strong></h4>
                    							<multiline label="Description"><p>'''+phone+'''</p></multiline>

                    						</td>
                    					</tr>
                    					</table>

                    				</td>
                    			</tr>
                    			</table>
                    			<br>
                    			</layout>

                    			<layout label="Article, tip or resource">
                    			<table width="100%" cellpadding="0" cellspacing="0" border="0">
                    			<tr>
                    				<td bgcolor="#ef3101" nowrap></td>
                    				<td width="100%" bgcolor="#ffffff">

                    					<table width="100%" cellpadding="20" cellspacing="0" border="0">
                    					<tr>
                    						<td bgcolor="#ffffff" class="contentblock">

                    							<h4 class="secondary"><strong><singleline label="Title">Почта отправителя</singleline></strong></h4>
                    							<multiline label="Description"><p>'''+post+'''</p></multiline>

                    						</td>
                    					</tr>
                    					</table>

                    				</td>
                    			</tr>
                    			</table>
                    			<br>
                    			</layout>



                    			<layout label="Article, tip or resource">
                                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                    <td bgcolor="#ef3101" nowrap></td>
                                    <td width="100%" bgcolor="#ffffff">

                                        <table width="100%" cellpadding="20" cellspacing="0" border="0">
                                        <tr>
                                            <td bgcolor="#ffffff" class="contentblock">

                                                <h4 class="secondary"><strong><singleline label="Title">Дата</singleline></strong></h4>
                                                <multiline label="Description"><p>'''+date+'''</p></multiline>

                                            </td>
                                        </tr>
                                        </table>

                                    </td>
                                </tr>
                                </table>
                                <br>
                                </layout>


                    			<layout label="Article, tip or resource">
                                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                    <td bgcolor="#ef3101" nowrap></td>
                                    <td width="100%" bgcolor="#ffffff">

                                        <table width="100%" cellpadding="20" cellspacing="0" border="0">
                                        <tr>
                                            <td bgcolor="#ffffff" class="contentblock">

                                                <h4 class="secondary"><strong><singleline label="Title">Прием</singleline></strong></h4>
                                                <multiline label="Description"><p>'''+priem+'''</p></multiline>

                                            </td>
                                        </tr>
                                        </table>

                                    </td>
                                </tr>
                                </table>
                                <br>
                                </layout>


                    			<layout label="Gallery highlights">
                    			<table width="100%" cellpadding="0" cellspacing="0" border="0">
                    			<tr>
                    				<td bgcolor="#832701" nowrap></td>
                    				<td width="100%" bgcolor="#ffffff">

                    					<table width="100%" cellpadding="20" cellspacing="0" border="0">
                    					<tr>
                    						<td bgcolor="#ffffff" class="contentblock">

                    							<h4 class="secondary"><strong><singleline label="Gallery title">Сообщение</singleline></strong></h4>
                    							<multiline label="Gallery description"><p>'''+message+'''</p></multiline>

                    						</td>
                    					</tr>
                    					</table>

                    				</td>
                    			</tr>
                    			</table>

                    			<table width="100%" cellpadding="0" cellspacing="0" border="0">

                    			</table>
                    <br>

                    		</repeater>

                    		</td>
                    	</tr>
                    	</table>

                    	<img border="0" src="images/spacer.gif" width="1" height="25" class="divider"><br>

                    	<table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f2f2f2">
                    	<tr>
                    		<td>

                    	<br>

                    			<table width="600" cellpadding="0" cellspacing="0" border="0" align="center" class="table">
                    			<tr>
                    				<td width="600" nowrap bgcolor="#f2f2f2" class="cell">

                    					<table width="600" cellpadding="0" cellspacing="0" border="0" class="table">
                    					<tr>
                    						<td width="380" valign="top" class="footershow">

                    							<br>

                    							<p style="color:#a6a6a6;font-size:12px;font-family:Helvetica,Arial,sans-serif;margin-top:0;margin-bottom:15px;padding-top:0;padding-bottom:0;line-height:18px;" class="reminder">© «Центр семейной медицины», 2010-2014<br>
                    Лицензия ЛО-66-01-003750 от 10.12.2015 <br><a href="http://www.cfm.ru/" style="color:#a6a6a6;text-decoration:underline;"> Перейти на сайт</a>.</p>

                    						</td>
                    						<td align="right" width="220" style="color:#a6a6a6;font-size:12px;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;text-shadow: 0 1px 0 #ffffff;" valign="top" class="hide">

                    							<table cellpadding="0" cellspacing="0" border="0">
                    							<tr>

                    								<td><a href="https://vk.com/club76276932"><img border="0" src="http://www.cfm.ru/img/vk.png" width="32" height="32" alt="Follow us on Twitter"></a></td>

                    							</tr>
                    							</table>


                    					</tr>
                    					</table>

                    				</td>
                    			</tr>
                    	   		</table>
                    <br>

                    	   </td>
                    	</tr>
                    	</table>

                    	</td>
                    </tr>
                    </table>

                    </body>
                    </html>
                    '''

                    return a

    def EMAIL_TEMPLATE_COM(name,city,post,phone,message):
        a = '''
        <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
       "http://www.w3.org/TR/html4/loose.dtd">

        <html lang="en">
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>Писимо с сайта (отзыв)</title>
            <style>
            a:hover {
                text-decoration: underline !important;
            }
            td.promocell p {
                color:#e1d8c1;
                font-size:16px;
                line-height:26px;
                font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
                margin-top:0;
                margin-bottom:0;
                padding-top:0;
                padding-bottom:14px;
                font-weight:normal;
            }
            td.contentblock h4 {
                color:#444444 !important;
                font-size:16px;
                line-height:24px;
                font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
                margin-top:0;
                margin-bottom:10px;
                padding-top:0;
                padding-bottom:0;
                font-weight:normal;
            }
            td.contentblock h4 a {
                color:#444444;
                text-decoration:none;
            }
            td.contentblock p {
                color:#888888;
                font-size:13px;
                line-height:19px;
                font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
                margin-top:0;
                margin-bottom:12px;
                padding-top:0;
                padding-bottom:0;
                font-weight:normal;
            }
            td.contentblock p a {
                color:#3ca7dd;
                text-decoration:none;
            }
            @media only screen and (max-device-width: 480px) {
                 div[class="header"] {
                      font-size: 16px !important;
                 }
                 table[class="table"], td[class="cell"] {
                      width: 300px !important;
                 }
                table[class="promotable"], td[class="promocell"] {
                      width: 325px !important;
                 }
                td[class="footershow"] {
                      width: 300px !important;
                 }
                table[class="hide"], img[class="hide"], td[class="hide"] {
                      display: none !important;
                 }
                 img[class="divider"] {
                      height: 1px !important;
                 }
                 td[class="logocell"] {
                    padding-top: 15px !important;
                    padding-left: 15px !important;
                    width: 300px !important;

                 }
                 img[id="screenshot"] {
                      width: 325px !important;
                      height: 127px !important;
                 }
                img[class="galleryimage"] {
                      width: 53px !important;
                      height: 53px !important;
                }
                p[class="reminder"] {
                    font-size: 11px !important;
                }
                h4[class="secondary"] {
                    line-height: 22px !important;
                    margin-bottom: 15px !important;
                    font-size: 18px !important;
                }
            }
            </style>
        </head>
        <body bgcolor="#e4e4e4" topmargin="0" leftmargin="0" marginheight="0" marginwidth="0" style="-webkit-font-smoothing: antialiased;width:100% !important;background:#e4e4e4;-webkit-text-size-adjust:none;">

        <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#e4e4e4">
        <tr>
            <td bgcolor="#e4e4e4" width="100%">

            <table width="600" cellpadding="0" cellspacing="0" border="0" align="center" class="table">
            <tr>
                <td width="600" class="cell">

                <table width="600" cellpadding="0" cellspacing="0" border="0" class="table">
                <tr>
                    <td style="background:#fff;padding:10px;" width="250" bgcolor="#e4e4e4" class="logocell"><br class="hide"><img src="http://www.cfm.ru/img/logo.png" width="100" height="60" alt="Campaign Monitor" style="-ms-interpolation-mode:bicubic;"><br></td>

                </tr>
                </table>


                <table width="600" cellpadding="25" cellspacing="0" border="0" class="promotable">
                <tr>
                    <td bgcolor="#4db1e2" width="600" class="promocell">

                        <multiline label="Main feature intro"><p style="color:#fff">Письмо с сайта (Связаться с нами)</p></multiline>

                    </td>
                </tr>
                </table>

                <br>

                <repeater>

                    <layout label="New feature">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#85bdad" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Имя отправителя</singleline></strong></h4>
                                    <multiline label="Description"><p>'''+name+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>

                    <layout label="New feature">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#85bdad" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Город</singleline></strong></h4>
                                    <multiline label="Description"><p>'''+city+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>

                    <layout label="Article, tip or resource">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#ef3101" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Почта отправителя</singleline></strong></h4>
                                    <multiline label="Description"><p>'''+post+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>

                    <layout label="Article, tip or resource">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#ef3101" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Телефон отправителя</singleline></strong></h4>
                                    <multiline label="Description"><p>'''+phone+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>

                    <layout label="Gallery highlights">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#832701" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Gallery title">Сообщение</singleline></strong></h4>
                                    <multiline label="Gallery description"><p>'''+message+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>

                    <table width="100%" cellpadding="0" cellspacing="0" border="0">

                    </table>
        <br>

                </repeater>

                </td>
            </tr>
            </table>

            <img border="0" src="images/spacer.gif" width="1" height="25" class="divider"><br>

            <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f2f2f2">
            <tr>
                <td>

            <br>

                    <table width="600" cellpadding="0" cellspacing="0" border="0" align="center" class="table">
                    <tr>
                        <td width="600" nowrap bgcolor="#f2f2f2" class="cell">

                            <table width="600" cellpadding="0" cellspacing="0" border="0" class="table">
                            <tr>
                                <td width="380" valign="top" class="footershow">

                                    <br>

                                    <p style="color:#a6a6a6;font-size:12px;font-family:Helvetica,Arial,sans-serif;margin-top:0;margin-bottom:15px;padding-top:0;padding-bottom:0;line-height:18px;" class="reminder">© «Центр семейной медицины», 2010-2014<br>
        Лицензия ЛО-66-01-003750 от 10.12.2015 <br><a href="http://www.cfm.ru/" style="color:#a6a6a6;text-decoration:underline;"> Перейти на сайт</a>.</p>

                                </td>
                                <td align="right" width="220" style="color:#a6a6a6;font-size:12px;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;text-shadow: 0 1px 0 #ffffff;" valign="top" class="hide">

                                    <table cellpadding="0" cellspacing="0" border="0">
                                    <tr>

                                        <td><a href="https://vk.com/club76276932"><img border="0" src="http://www.cfm.ru/img/vk.png" width="32" height="32" alt="Follow us on Twitter"></a></td>

                                    </tr>
                                    </table>


                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
        <br>

               </td>
            </tr>
            </table>

            </td>
        </tr>
        </table>

        </body>
        </html>
        '''

        return a






    def EMAIL_TEMPLATE_ANKETA(name,born,post,phone,skype,date,time,price,theme):
        a = '''
        <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
       "http://www.w3.org/TR/html4/loose.dtd">

        <html lang="en">
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>Писимо с сайта (отзыв)</title>
            <style>
            a:hover {
                text-decoration: underline !important;
            }
            td.promocell p {
                color:#e1d8c1;
                font-size:16px;
                line-height:26px;
                font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
                margin-top:0;
                margin-bottom:0;
                padding-top:0;
                padding-bottom:14px;
                font-weight:normal;
            }
            td.contentblock h4 {
                color:#444444 !important;
                font-size:16px;
                line-height:24px;
                font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
                margin-top:0;
                margin-bottom:10px;
                padding-top:0;
                padding-bottom:0;
                font-weight:normal;
            }
            td.contentblock h4 a {
                color:#444444;
                text-decoration:none;
            }
            td.contentblock p {
                color:#888888;
                font-size:13px;
                line-height:19px;
                font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
                margin-top:0;
                margin-bottom:12px;
                padding-top:0;
                padding-bottom:0;
                font-weight:normal;
            }
            td.contentblock p a {
                color:#3ca7dd;
                text-decoration:none;
            }
            @media only screen and (max-device-width: 480px) {
                 div[class="header"] {
                      font-size: 16px !important;
                 }
                 table[class="table"], td[class="cell"] {
                      width: 300px !important;
                 }
                table[class="promotable"], td[class="promocell"] {
                      width: 325px !important;
                 }
                td[class="footershow"] {
                      width: 300px !important;
                 }
                table[class="hide"], img[class="hide"], td[class="hide"] {
                      display: none !important;
                 }
                 img[class="divider"] {
                      height: 1px !important;
                 }
                 td[class="logocell"] {
                    padding-top: 15px !important;
                    padding-left: 15px !important;
                    width: 300px !important;

                 }
                 img[id="screenshot"] {
                      width: 325px !important;
                      height: 127px !important;
                 }
                img[class="galleryimage"] {
                      width: 53px !important;
                      height: 53px !important;
                }
                p[class="reminder"] {
                    font-size: 11px !important;
                }
                h4[class="secondary"] {
                    line-height: 22px !important;
                    margin-bottom: 15px !important;
                    font-size: 18px !important;
                }
            }
            </style>
        </head>
        <body bgcolor="#e4e4e4" topmargin="0" leftmargin="0" marginheight="0" marginwidth="0" style="-webkit-font-smoothing: antialiased;width:100% !important;background:#e4e4e4;-webkit-text-size-adjust:none;">

        <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#e4e4e4">
        <tr>
            <td bgcolor="#e4e4e4" width="100%">

            <table width="600" cellpadding="0" cellspacing="0" border="0" align="center" class="table">
            <tr>
                <td width="600" class="cell">

                <table width="600" cellpadding="0" cellspacing="0" border="0" class="table">
                <tr>
                    <td style="background:#fff;padding:10px;" width="250" bgcolor="#e4e4e4" class="logocell"><br class="hide"><img src="http://www.cfm.ru/img/logo.png" width="100" height="60" alt="Campaign Monitor" style="-ms-interpolation-mode:bicubic;"><br></td>

                </tr>
                </table>


                <table width="600" cellpadding="25" cellspacing="0" border="0" class="promotable">
                <tr>
                    <td bgcolor="#4db1e2" width="600" class="promocell">

                        <multiline label="Main feature intro"><p style="color:#fff">Письмо с сайта (Запись)</p></multiline>

                    </td>
                </tr>
                </table>

                <br>

                <repeater>

                    <layout label="New feature">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#85bdad" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Имя отправителя</singleline></strong></h4>
                                    <multiline label="Description"><p>'''+name+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>

                    <layout label="New feature">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#85bdad" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Дата рождения </singleline></strong></h4>
                                    <multiline label="Description"><p>'''+born+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>

                    <layout label="Article, tip or resource">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#ef3101" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Почта отправителя</singleline></strong></h4>
                                    <multiline label="Description"><p>'''+post+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>

                    <layout label="Article, tip or resource">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#ef3101" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Телефон отправителя</singleline></strong></h4>
                                    <multiline label="Description"><p>'''+phone+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>




                    <layout label="Article, tip or resource">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#ef3101" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Skype отправителя</singleline></strong></h4>
                                    <multiline label="Description"><p>'''+skype+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>


                    <layout label="Article, tip or resource">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#ef3101" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Желаемая дата</singleline></strong></h4>
                                    <multiline label="Description"><p>'''+date+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>





                    <layout label="Article, tip or resource">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#ef3101" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Желаемое время консультации</singleline></strong></h4>
                                    <multiline label="Description"><p>'''+time+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>





                    <layout label="Article, tip or resource">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#ef3101" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Ф.И.О. плательщика</singleline></strong></h4>
                                    <multiline label="Description"><p>'''+price+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>




                    <layout label="Article, tip or resource">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td bgcolor="#ef3101" nowrap></td>
                        <td width="100%" bgcolor="#ffffff">

                            <table width="100%" cellpadding="20" cellspacing="0" border="0">
                            <tr>
                                <td bgcolor="#ffffff" class="contentblock">

                                    <h4 class="secondary"><strong><singleline label="Title">Тема консультации</singleline></strong></h4>
                                    <multiline label="Description"><p>'''+theme+'''</p></multiline>

                                </td>
                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
                    <br>
                    </layout>



                    <table width="100%" cellpadding="0" cellspacing="0" border="0">

                    </table>
                    <br>

                </repeater>

                </td>
            </tr>
            </table>

            <img border="0" src="images/spacer.gif" width="1" height="25" class="divider"><br>

            <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f2f2f2">
            <tr>
                <td>

            <br>

                    <table width="600" cellpadding="0" cellspacing="0" border="0" align="center" class="table">
                    <tr>
                        <td width="600" nowrap bgcolor="#f2f2f2" class="cell">

                            <table width="600" cellpadding="0" cellspacing="0" border="0" class="table">
                            <tr>
                                <td width="380" valign="top" class="footershow">

                                    <br>

                                    <p style="color:#a6a6a6;font-size:12px;font-family:Helvetica,Arial,sans-serif;margin-top:0;margin-bottom:15px;padding-top:0;padding-bottom:0;line-height:18px;" class="reminder">© «Центр семейной медицины», 2010-2014<br>
        Лицензия ЛО-66-01-003750 от 10.12.2015 <br><a href="http://www.cfm.ru/" style="color:#a6a6a6;text-decoration:underline;"> Перейти на сайт</a>.</p>

                                </td>
                                <td align="right" width="220" style="color:#a6a6a6;font-size:12px;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;text-shadow: 0 1px 0 #ffffff;" valign="top" class="hide">

                                    <table cellpadding="0" cellspacing="0" border="0">
                                    <tr>

                                        <td><a href="https://vk.com/club76276932"><img border="0" src="http://www.cfm.ru/img/vk.png" width="32" height="32" alt="Follow us on Twitter"></a></td>

                                    </tr>
                                    </table>


                            </tr>
                            </table>

                        </td>
                    </tr>
                    </table>
        <br>

               </td>
            </tr>
            </table>

            </td>
        </tr>
        </table>

        </body>
        </html>
        '''

        return a

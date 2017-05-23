
<!DOCTYPE html>
<html>
	<head>
		<title>ЦСМ</title>	
		<!-- metas -->
		<meta charset="utf-8">
		<meta name="author" content="">
		<meta name="keywords" content="ЦСМ">
		<meta name="description" content="">
		<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
		<!--/ metas -->
		
		<!-- styles -->
		<link rel="stylesheet" type="text/css" href="css/layerslider.css">
		<link rel="stylesheet" type="text/css" href="css/fullwidth/skin.css">
		<link rel="stylesheet" type="text/css" href="css/font-awesome.css">
		<link rel="stylesheet" type="text/css" href="css/owl.carousel.css">
		<link rel="stylesheet" type="text/css" href="css/jquery.fancybox.css">
		<link rel="stylesheet" type="text/css" href="css/styles.css">
		<link rel="stylesheet" type="text/css" href="css/color-blue.css">
		
		<!--/ styles -->
		
		<!--[if lt IE 9]><script src="js/html5.js"></script><![endif]-->
	</head>
	
	<body>
		<div class="page">
            <!-- page header -->

<!--/ page header -->
			

			
			
			<!-- page title -->
			<section class="page-title">
				<div class="grid-row clearfix">
					<h1>Сообщение специалисту</h1>					
					<nav class="bread-crumbs">
						<a href="index.php">Главное</a>&nbsp;&nbsp;<i class="fa fa-angle-right"></i>&nbsp;
						<a href="#">Сообщение специалисту</a>
					</nav>
				</div>
			</section>
			<!--/ page title -->

			<main class="page-content">
				<div class="grid-row">
	


                    
					</div>
                
                <!-- Comment Form -->
                <a class="anchor" name="comment"></a>
                <div class="grid-row">
                <br/>
                <br/>
                
                <section class="widget widget-appointment">                      
							<form action="/form/mail_special.php" name="contactform" method="post">
                                
									<input type="hidden" name="doc" value="<?php echo $_GET['docemail']; ?>">
									
								
								<div class="row">
									<input type="text" name="name" placeholder="имя">
									<i class="fa fa-user"></i>
								</div>
								<div class="row">
									<input type="email" name="email" placeholder="электронная почта">
									<i class="fa fa-envelope"></i>
								</div>							
								<div class="row">
									<textarea cols="30" rows="10" name="message" placeholder="сообщение"></textarea>
									<i class="fa fa-align-left"></i>
								</div>
								  <button type="submit" name="submit" class="button" value="Submit">Отправить</button>
							</form>
						</section>
                    </div>
                
                <!--/ Comment Form -->
               

				</div>
			</main>
            <!-- page footer -->

			<!--/ page footer -->
			
			

		</div>
		
		<!-- scripts -->
		<script type="text/javascript" src="js/jquery.min.js"></script>
		<script type="text/javascript" src="js/jquery-ui.min.js"></script>
		<script type="text/javascript" src="js/jquery.migrate.min.js"></script>
		<script type="text/javascript" src="js/owl.carousel.min.js"></script>
		<script type="text/javascript" src="js/jquery.isotope.min.js"></script>
		<script type="text/javascript" src="js/jquery.fancybox.pack.js"></script>
		<script type="text/javascript" src="js/jquery.fancybox-media.js"></script>
		<script type="text/javascript" src="js/jquery.flot.js"></script>
		<script type="text/javascript" src="js/jquery.flot.pie.js"></script>
		<script type="text/javascript" src="js/jquery.flot.categories.js"></script>
		<script type="text/javascript" src="js/greensock.js"></script>
		<script type="text/javascript" src="js/layerslider.transitions.js"></script>
		<script type="text/javascript" src="js/layerslider.kreaturamedia.jquery.js"></script>

	<!-- Superscrollorama -->		
		<script type="text/javascript" src="js/jquery.superscrollorama.js"></script>
		<script type="text/javascript" src="js/TweenMax.min.js"></script>
		<script type="text/javascript" src="js/TimelineMax.min.js"></script>
	<!--/ Superscrollorama -->
	
		<script type="text/javascript" src="js/jquery.ui.core.min.js"></script>
		<script type="text/javascript" src="js/jquery.ui.widget.min.js"></script>
		<script type="text/javascript" src="js/jquery.ui.tabs.min.js"></script>
		<script type="text/javascript" src="js/jquery-ui-tabs-rotate.js"></script>
		<script type="text/javascript" src="js/jquery.ui.accordion.min.js"></script>
		<script type="text/javascript" src="js/jquery.tweet.js"></script>
	<!-- EASYPIECHART -->
		<script type="text/javascript" src="js/jquery.easypiechart.js"></script>
	<!--/ EASYPIECHART -->
		<script type="text/javascript" src="js/scripts.js"></script>
		<!--/ scripts -->
		
	</body>
</html>

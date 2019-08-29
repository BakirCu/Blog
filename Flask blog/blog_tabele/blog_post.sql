CREATE DATABASE  IF NOT EXISTS `blog` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `blog`;
-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: blog
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `posts` (
  `title` varchar(45) NOT NULL,
  `time_post` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  `post` varchar(13000) NOT NULL,
  `image` longblob,
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES ('sddadas','2019-08-04 14:27:10',99,'bakir',NULL),('sddadas','2019-08-04 14:27:12',100,'bakir',NULL),('sddadas','2019-08-04 14:27:12',101,'bakir',NULL),('sddadas','2019-08-04 14:27:12',102,'bakir',NULL),('ivana prica o hrani','2019-08-06 20:56:15',103,'sdkjdjasjdljasdjasjdasjdkl',NULL),('sdad','2019-08-06 20:57:00',104,'sadasdasdas',NULL),('asdasd','2019-08-06 20:57:16',105,'asdsadasdas',NULL),('sdadasas','2019-08-06 20:57:32',106,'asddasdas',NULL),('bakir','2019-08-12 22:50:27',107,'s',NULL),('bakir','2019-08-12 22:50:57',108,'dsadad',NULL),('bakir','2019-08-12 22:51:12',109,'sadasdas',NULL),('nemanja','2019-08-14 12:00:35',110,'dasdsads\r\n',NULL),('bakir','2019-08-18 17:31:24',111,'kkkkk',NULL),('timur','2019-08-18 17:34:46',112,'s',NULL),('bakir','2019-08-18 17:36:32',113,'sss',NULL),('amra','2019-08-18 17:39:38',114,'sdsdasd',NULL),('nemanja','2019-08-18 17:46:23',115,'n',NULL),('timur','2019-08-19 21:46:18',116,'sdasdasda\r\n',NULL),('bakir','2019-08-19 21:51:32',117,'jjjjj',NULL),('jlkjljljlkjkklkljkj','2019-08-21 22:40:23',118,'iyiuyuiyuiyuiyuiyuiuiyui',NULL),('fetrsrftrtrd','2019-08-21 22:46:42',119,'ui423353466897',NULL),('amra','2019-08-29 14:52:48',121,'jsjsjsjjs',_binary '‰PNG\r\n\Z\n\0\0\0\rIHDR\0\0\0\á\0\0\0\á\0\0\0	m\"H\0\0\0¢PLTE÷\ß\0\0\0bXÿ\çú\âË·ý\äOG	UL	`Vÿ\èXO\nTK	]S\nZQ\n]T\n\ï\Ø‘ƒ\ì\ÕÈµ¡‘Â¯\ã\Í°Ÿ¶¤|o†y\ÕÀ\Z˜‰\à\Ê¨—»©nc}q4/\Ù\Ä\Z*&th\r›Œ„wG@od\rh]E>;5¬› &\"\n	50.)+¿2\Ø\0\0\reIDATxœ\í]iƒ¢¸$Ä°…E\ÅmG­.»\ÛY\Þüÿ¿öpC\Å2ôp>uµ[Žw¿¹‰\0t\èÐ¡C‡:t\è\Ð\á÷\0\Â\ï^ÁkQ<O(\"Œ†ûB\ï^Uc@\Ø;jôF»©fb[+?!þ-H\"\Î	u|p8#–ch	—’\Õ1l?G3\âhZ?@pL\\-ƒ’õ\0¶›#ý>§E‡ûD\Ë\Ã +¾{•\á³\Øh\0ç–€ \çh\Ï[+ElO¬\è\Ò\\Š$xztû\î•>8 Æ™\ZØ…5\ÍY·RŠxx!E\ÇaŠž`[˜ ÿ†T \ÅôŠÞ»\×[·Ž\Å\ï\Ýv‰”\'m\"ž\Ü:–™SAP3ö-cˆ²v\'VQ—R‹0\Ð$`¶\Ì\×Àm…Ý±lF\ÛG›\Ðó\Â\Ñp¥ivð\î5\×?.<‹L\Ç\0¡	¢á§•Èl\Ú%\ÄR\éY³‘1†a|“ˆ[ma˜Ô¹xB‹ø9d{˜!oS\ái­bˆ¾\ÙJ\Z”\î¬&„^<µi\ÖRÉ¢\Z­óx,dhX‡	«õ1Š|‹\æ‘Ý‚õ1Œ5[¡A>Œö&«û*1yø ¼±7#L04F\"+4\ÈVÇˆUûC’‡\ë«ñ\áÀIò\âtÈ­\ß:?¸ðIQrcÔ–!Bó´Žp÷\î\Ëj\Ä	¿™]œRµ\ÍyÛ“br%½Kg\\2ôx\Ê™\ßŽ\ÚJŠ\îyñV€¢l:C\Ö!dFº+‘ƒ­t¬Àºu–š1\Å0S(9t\ÄMœ\Â ýPe\âÑµ?Apq+B\Ûg\n\n£Uy¯¹[¥%xCP³\"s~õ–®;\à\nê“ª:Cóf˜!¨\ÙÀ»þIö\\€£²úU\Ú±~K\ÐØšË³Ád™“v³ º\ÂFˆsvè¬Ž¶\à¨U\nP\ë&\È2ÐŒ‰\ÑQ|bl\íY€†ýJ~š«\Ü\Ó\Çw&kqJ\Øl\æýq°-- Ž\ïŒ\ÌMsnƒ\êi(­\ê ò‚Je(\Èy‘U\ÂS™\Çe]ü\è*T™ Àk¡\è\Öc&(\áC\r{¨ö>wNGSX3\ÆÏ«6AƒLJ\0OH‚pjU&h^1¾›B9ðNÄŒYž‰\Ëø+²Už@¡HGû,¸a½¼L‰3\Ü(\Ï\08(\"a™6ŒÂ¼a¸\Ô\"\Ú~¼Á-\à\Ç\Ò5 l\Ü\àe\Ï\Ép¬(¥\Æa\ê!HGhò$±@„<ƒ†—0\èƒ+90/†\â\r\ïh©t\ç\ÉQ˜\ç‰\ÇW\Ñ:tzŒ<ñ,Œ,¢x8;XK•	‚U\0‡¹šÁ\ÎH0\ÕSjÙ‡ý|™`\çÏ¦+\Ç&u\\\×Rz„MW\ätô^‚WšŽÃ¬:Œ—q\n\"ôS\éd\rúö\ÎÌµD\íQN‚…°\çJ\'kxL\èÈ¼<\àõ<Ž¥ºt ²†´±5;ôî¸%#X:t}\ê:PYC†æ˜£l\ÂF\ç\æ]Ã¦†¥tEÏ€—Tsg¦ŸQRg˜l+Z¢\éW¡¶‹§d”ŽQ&±6V¼®J¶9\ì\Ò.†ú\ïúnnƒ‚a,ª	\Z–\Ú.†#MF-/³‰\Í÷\ßÑ¶º%£z\Ç\"\æ\"\Ô\æmNJX \Ä~uSø\Êk(CÀÝ¥±7oœ\n³z©d6ö¬¡v+ó\Òg\\\ã‚;Ew;B8\Õ[2)ð\'w\'4Ö¯2t=t\×\ØÁöA4ôÒ·°¢«£!^\Õl¬cŒ”÷¡)Pœ0#\á%\Þ[K\æe\Ö\å{/®=÷Z¡¡€m§\ã$Á\çIh\î”{™Ru\íÙ¢%—\Æ	\Î\"tT\ÚWc°¿P¾s¸2R†\'R¬\æE\â®pÊŸ\Æ^»üÀ”¥z\éø•ûE¹¥~„\Ûbg\à´JS‡chŒó±\ÈW10[%¾i`wR‡cGˆW\ÃEð\Çz\0p+Z¿7Hù³$\î³l\r”I{{\ê\ãw/ZÀ“Ä’]P®£óª|Ûµ?Už#\Ésu U¥£–6j‘–¢I8½0tf\å:Ê•\Ù\Ò\â6\ÔK°\â×¹2²\0‡e:jCZ,ð­úM°p\ï\é\"b{¯·.|\È3V¬(œ\é¨k»\Ö\Ðö\0„ðZ²PXt\êÇµ\ì\Ù\0´ch8\Ó\Ýñ,C—»;J4¿ô\0w3¶\á\\”\Ô\nQöÈˆa8Ô²\él¼i\'=Ž\Û\Ñ:„À\ã:\Äf \Îa»žOô¶-E\Ë^Gô,f•;ö—³¼\0·œ\\\n\ïÌñ\é|¨3jWõW«ó<õö5\Þ\äm[P/L ö\áy`\Æa‰\Ù\ï\Ãñœ\Äð\Þþµ°·\ï7°Á˜»z\É×Œ.±ü—Žpññ›\Ó0Î«\ï$Â¼{á²Û–£\Óõô„\í\çL¯üh„ó¨üH„!\Ø\Ä\Ã\Ùöós»\Ýû\ãA\0^y)b\å!c~\Ðp0w\í-0\áÕŸŠ3ÿ=}\Þ\ïeñƒ7\æ‹H¢IDxúð\ÍðP§|Gƒ^e­bdnfù—¤,\ç\áKš\Ìü\nº¼|\íü4oW#=¿\Ò~\É:ÍVÀ/Á\Úkž#\â;\Û$s\íA]©\Ç{\ë2~\Íñ\áúsµ\ÂQ?†š\Þ3X¢f?~\'@†Ð— \È\Ð\ìž>R~zò\á\×\×`ˆr{½q“‘ö\Üiky†Ð%\Ø\ëÍ‡”_ SR\ë	Û–fhn\å	öz“Æ¤È·\Ý¦-\Ë\ë\ìõ¢¦<*Ÿ¾x\êfI†hS`¯\×\Ð)þ\Ä\ÏlŸñÎ’\Í_ujÍ˜\"¿â¹»¸\ä\âI]‚\Ì›‹\É\Ï]®\"\ÇýYŸa#z\Êó™\'/“bøˆ{½F\î* O_=\"\Å\Ðü(¤ñý{Á?š8d›\ÜUò\ä¥2Q &q±\Â›ñ}±È°n¤\Æ/º°\ã\ç\ÞI†!>Šøõ\Ã\Ó\È\Â\æ\æN\ÈÿF\ÍxR&\Ç&Ÿ‚C¸4n{²(›”7UA¡!O\ç¸R2ü7ÿœ_wß¬y\Íy>\Z\'Ã¾¶yZÙ¥<@„¹—¹>=²l®\áŽF\r(ƒCQ\ÆöW\Þ\Î`b‹n£\ÇRšø®d\nšUSA\ê\Z²ÿ\Õ\Û1‘a(\è]ˆô*n—<(CaÁ¦\æV‰CÁSöí™¾•a\åŸbÿ^\ÃüSš*p¿\0\ÆC¿¹^Ó‹!•y‹ª\Ãç“/‚T^j	ö\Úq\ØF2/÷º\ãvŒSKiiÁv\Å*hƒG•\ëÓˆ2Ó‚S\rRañž\á:T]W¥Šò¶¨´Ï‘\ì—þUB±÷«Ì±¡ŽðN]ƒ”\í\ê—\n‘c*\ÊQvgF}\ß\ã)\ét¤w\×dv¸?\"\å(½C\nm\ß<Œ…rr¬±ÿ‡\Å\ÞVµR\ä¢\ào)Š½¥Zb¬!C:\Ã\"üT\êŠ:ó4\Ør{c…\ê\ãzS_¦\ä\ÌP\ï‰	Ÿ¦Qsr\ê’\Æh)s<®\îl\"{9Š?U¹¢.C&Æ…œ5~(¢¨õd\ê?e(®\Ôp70\ä¢ŽC%š1\ä#\Ñ\Æð”8Mý C\Î\Ñó«ü\êOôôa†€û\ÕqE®ª\ÂU¨\Ï0dÍ°[|\Æ/,ñ9†\\Y\ëŠ\ra>ŽgrŽAq°}¿Ÿg˜p,”\ã\ïÁÁ\\´\0Þ¯¦\r1d‰\Î\\\Èðý?¦\ÔC&FaOõðv5mŽ¡¸x¼Ÿûz4\È`Qüov¹ Q†cÃ·4ˆ¶•\nû40,õŒ\ÂI\Ûò—4\nq[A´¿k‰B\Ê%¿\î‡ha$œ&i–&bˆ=ž¹”Ÿ¢€ÿ\äß¬ú$r3À`*6z¼\Ë/J4xˆ—\éc¥#»P\àj¾&\ä#˜HJt~\æ•û\ÕJõK3¸¬ªE\ï\Ò\ÒË ¹`u¢	\çû<†7ûøß‹/P¸þ¾ô¦ÿ—¿h!XT¶n\Å \Éÿ*¤hŠjÅ—p\ÊP0\ã›^\Ã\ì\ÞQ˜¢\Â\çV±9¹\ïUüQ°»cÁ{½<§w9ÿ2KQ(\Â\ÞÍ¢`$p½‘È£B\á6ñ\çkóRŒr©bf\ë\Ñn\ÒMÀž´`\Ø\æ8ñ\î_*Csô#ÿ‘‡\0^ŽºD\Â\í²WŠ\Å%\ÃlqsG+\"~\ÞKS\Z¯ I4Õ“Ÿ<Z\ÄG—3\ìE{ý\î!œÜ½¡û\ß\nžô\í¥ýD\\ô±½Þ\Ò=\áû­^\áŠ;¾}ôKO—¾¶\0.\Z)¬@6Þ›Ò‡ð…xq4„ô‘E\Ý[N±´«ñ\ê‘~\áz\î\Û2³B…xyBS÷=G.³ƒ‘Mð\ÚP‘®®¶ž\Î3m‚òC\nufÃ¨¹¨\ï¢÷žO¸Ã—40êš¢¸š+\è…V\à‹ª{\\ëº‡¢;„Iu¾\ì÷„\ëP,Þ–Æ‹¢S\éEˆ¾®QŠe‡µ\î¨u{Ë¯/\ßCh-µªŠ_>4u\ÙoŠ\çE_¼!c\êÕ““n\å– x”\Ëoú¯¹¶­|qhY¾¨?¥ðb4)\Î\æ\Ïø\Ð\ß3(ŒÁ²xqýØ”4ln\Öe‚ü{½y\ßt)\Æ\ÑL\äûÃ°\Îq	Q4\Ï}}óuð\ÞAoVŠñüðq\âù÷¯þvú÷9²÷Á›‰¯õ/ZñGºÔ½W\ÝYoq¼*G ¹G`™\Ë1‹\Þc\ÈU;½’™¯¼Ü³C‡:t\èÐ¡C‡:t\èÐ¡C‡:t\èÐ¡C‡ÿüH¹\Ìl!\Ùø\Ö\0\0\0\0IEND®B`‚'),('amra','2019-08-29 17:37:28',122,'jsjsjsjjs',_binary '‰PNG\r\n\Z\n\0\0\0\rIHDR\0\0\0\á\0\0\0\á\0\0\0	m\"H\0\0\0¢PLTE÷\ß\0\0\0bXÿ\çú\âË·ý\äOG	UL	`Vÿ\èXO\nTK	]S\nZQ\n]T\n\ï\Ø‘ƒ\ì\ÕÈµ¡‘Â¯\ã\Í°Ÿ¶¤|o†y\ÕÀ\Z˜‰\à\Ê¨—»©nc}q4/\Ù\Ä\Z*&th\r›Œ„wG@od\rh]E>;5¬› &\"\n	50.)+¿2\Ø\0\0\reIDATxœ\í]iƒ¢¸$Ä°…E\ÅmG­.»\ÛY\Þüÿ¿öpC\Å2ôp>uµ[Žw¿¹‰\0t\èÐ¡C‡:t\è\Ð\á÷\0\Â\ï^ÁkQ<O(\"Œ†ûB\ï^Uc@\Ø;jôF»©fb[+?!þ-H\"\Î	u|p8#–ch	—’\Õ1l?G3\âhZ?@pL\\-ƒ’õ\0¶›#ý>§E‡ûD\Ë\Ã +¾{•\á³\Øh\0ç–€ \çh\Ï[+ElO¬\è\Ò\\Š$xztû\î•>8 Æ™\ZØ…5\ÍY·RŠxx!E\ÇaŠž`[˜ ÿ†T \ÅôŠÞ»\×[·Ž\Å\ï\Ýv‰”\'m\"ž\Ü:–™SAP3ö-cˆ²v\'VQ—R‹0\Ð$`¶\Ì\×Àm…Ý±lF\ÛG›\Ðó\Â\Ñp¥ivð\î5\×?.<‹L\Ç\0¡	¢á§•Èl\Ú%\ÄR\éY³‘1†a|“ˆ[ma˜Ô¹xB‹ø9d{˜!oS\ái­bˆ¾\ÙJ\Z”\î¬&„^<µi\ÖRÉ¢\Z­óx,dhX‡	«õ1Š|‹\æ‘Ý‚õ1Œ5[¡A>Œö&«û*1yø ¼±7#L04F\"+4\ÈVÇˆUûC’‡\ë«ñ\áÀIò\âtÈ­\ß:?¸ðIQrcÔ–!Bó´Žp÷\î\Ëj\Ä	¿™]œRµ\ÍyÛ“br%½Kg\\2ôx\Ê™\ßŽ\ÚJŠ\îyñV€¢l:C\Ö!dFº+‘ƒ­t¬Àºu–š1\Å0S(9t\ÄMœ\Â ýPe\âÑµ?Apq+B\Ûg\n\n£Uy¯¹[¥%xCP³\"s~õ–®;\à\nê“ª:Cóf˜!¨\ÙÀ»þIö\\€£²úU\Ú±~K\ÐØšË³Ád™“v³ º\ÂFˆsvè¬Ž¶\à¨U\nP\ë&\È2ÐŒ‰\ÑQ|bl\íY€†ýJ~š«\Ü\Ó\Çw&kqJ\Øl\æýq°-- Ž\ïŒ\ÌMsnƒ\êi(­\ê ò‚Je(\Èy‘U\ÂS™\Çe]ü\è*T™ Àk¡\è\Öc&(\áC\r{¨ö>wNGSX3\ÆÏ«6AƒLJ\0OH‚pjU&h^1¾›B9ðNÄŒYž‰\Ëø+²Už@¡HGû,¸a½¼L‰3\Ü(\Ï\08(\"a™6ŒÂ¼a¸\Ô\"\Ú~¼Á-\à\Ç\Ò5 l\Ü\àe\Ï\Ép¬(¥\Æa\ê!HGhò$±@„<ƒ†—0\èƒ+90/†\â\r\ïh©t\ç\ÉQ˜\ç‰\ÇW\Ñ:tzŒ<ñ,Œ,¢x8;XK•	‚U\0‡¹šÁ\ÎH0\ÕSjÙ‡ý|™`\çÏ¦+\Ç&u\\\×Rz„MW\ätô^‚WšŽÃ¬:Œ—q\n\"ôS\éd\rúö\ÎÌµD\íQN‚…°\çJ\'kxL\èÈ¼<\àõ<Ž¥ºt ²†´±5;ôî¸%#X:t}\ê:PYC†æ˜£l\ÂF\ç\æ]Ã¦†¥tEÏ€—Tsg¦ŸQRg˜l+Z¢\éW¡¶‹§d”ŽQ&±6V¼®J¶9\ì\Ò.†ú\ïúnnƒ‚a,ª	\Z–\Ú.†#MF-/³‰\Í÷\ßÑ¶º%£z\Ç\"\æ\"\Ô\æmNJX \Ä~uSø\Êk(CÀÝ¥±7oœ\n³z©d6ö¬¡v+ó\Òg\\\ã‚;Ew;B8\Õ[2)ð\'w\'4Ö¯2t=t\×\ØÁöA4ôÒ·°¢«£!^\Õl¬cŒ”÷¡)Pœ0#\á%\Þ[K\æe\Ö\å{/®=÷Z¡¡€m§\ã$Á\çIh\î”{™Ru\íÙ¢%—\Æ	\Î\"tT\ÚWc°¿P¾s¸2R†\'R¬\æE\â®pÊŸ\Æ^»üÀ”¥z\éø•ûE¹¥~„\Ûbg\à´JS‡chŒó±\ÈW10[%¾i`wR‡cGˆW\ÃEð\Çz\0p+Z¿7Hù³$\î³l\r”I{{\ê\ãw/ZÀ“Ä’]P®£óª|Ûµ?Už#\Ésu U¥£–6j‘–¢I8½0tf\å:Ê•\Ù\Ò\â6\ÔK°\â×¹2²\0‡e:jCZ,ð­úM°p\ï\é\"b{¯·.|\È3V¬(œ\é¨k»\Ö\Ðö\0„ðZ²PXt\êÇµ\ì\Ù\0´ch8\Ó\Ýñ,C—»;J4¿ô\0w3¶\á\\”\Ô\nQöÈˆa8Ô²\él¼i\'=Ž\Û\Ñ:„À\ã:\Äf \Îa»žOô¶-E\Ë^Gô,f•;ö—³¼\0·œ\\\n\ïÌñ\é|¨3jWõW«ó<õö5\Þ\äm[P/L ö\áy`\Æa‰\Ù\ï\Ãñœ\Äð\Þþµ°·\ï7°Á˜»z\É×Œ.±ü—Žpññ›\Ó0Î«\ï$Â¼{á²Û–£\Óõô„\í\çL¯üh„ó¨üH„!\Ø\Ä\Ã\Ùöós»\Ýû\ãA\0^y)b\å!c~\Ðp0w\í-0\áÕŸŠ3ÿ=}\Þ\ïeñƒ7\æ‹H¢IDxúð\ÍðP§|Gƒ^e­bdnfù—¤,\ç\áKš\Ìü\nº¼|\íü4oW#=¿\Ò~\É:ÍVÀ/Á\Úkž#\â;\Û$s\íA]©\Ç{\ë2~\Íñ\áúsµ\ÂQ?†š\Þ3X¢f?~\'@†Ð— \È\Ð\ìž>R~zò\á\×\×`ˆr{½q“‘ö\Üiky†Ð%\Ø\ëÍ‡”_ SR\ë	Û–fhn\å	öz“Æ¤È·\Ý¦-\Ë\ë\ìõ¢¦<*Ÿ¾x\êfI†hS`¯\×\Ð)þ\Ä\ÏlŸñÎ’\Í_ujÍ˜\"¿â¹»¸\ä\âI]‚\Ì›‹\É\Ï]®\"\ÇýYŸa#z\Êó™\'/“bøˆ{½F\î* O_=\"\Å\Ðü(¤ñý{Á?š8d›\ÜUò\ä¥2Q &q±\Â›ñ}±È°n¤\Æ/º°\ã\ç\ÞI†!>Šøõ\Ã\Ó\È\Â\æ\æN\ÈÿF\ÍxR&\Ç&Ÿ‚C¸4n{²(›”7UA¡!O\ç¸R2ü7ÿœ_wß¬y\Íy>\Z\'Ã¾¶yZÙ¥<@„¹—¹>=²l®\áŽF\r(ƒCQ\ÆöW\Þ\Î`b‹n£\ÇRšø®d\nšUSA\ê\Z²ÿ\Õ\Û1‘a(\è]ˆô*n—<(CaÁ¦\æV‰CÁSöí™¾•a\åŸbÿ^\ÃüSš*p¿\0\ÆC¿¹^Ó‹!•y‹ª\Ãç“/‚T^j	ö\Úq\ØF2/÷º\ãvŒSKiiÁv\Å*hƒG•\ëÓˆ2Ó‚S\rRañž\á:T]W¥Šò¶¨´Ï‘\ì—þUB±÷«Ì±¡ŽðN]ƒ”\í\ê—\n‘c*\ÊQvgF}\ß\ã)\ét¤w\×dv¸?\"\å(½C\nm\ß<Œ…rr¬±ÿ‡\Å\ÞVµR\ä¢\ào)Š½¥Zb¬!C:\Ã\"üT\êŠ:ó4\Ør{c…\ê\ãzS_¦\ä\ÌP\ï‰	Ÿ¦Qsr\ê’\Æh)s<®\îl\"{9Š?U¹¢.C&Æ…œ5~(¢¨õd\ê?e(®\Ôp70\ä¢ŽC%š1\ä#\Ñ\Æð”8Mý C\Î\Ñó«ü\êOôôa†€û\ÕqE®ª\ÂU¨\Ï0dÍ°[|\Æ/,ñ9†\\Y\ëŠ\ra>ŽgrŽAq°}¿Ÿg˜p,”\ã\ïÁÁ\\´\0Þ¯¦\r1d‰\Î\\\Èðý?¦\ÔC&FaOõðv5mŽ¡¸x¼Ÿûz4\È`Qüov¹ Q†cÃ·4ˆ¶•\nû40,õŒ\ÂI\Ûò—4\nq[A´¿k‰B\Ê%¿\î‡ha$œ&i–&bˆ=ž¹”Ÿ¢€ÿ\äß¬ú$r3À`*6z¼\Ë/J4xˆ—\éc¥#»P\àj¾&\ä#˜HJt~\æ•û\ÕJõK3¸¬ªE\ï\Ò\ÒË ¹`u¢	\çû<†7ûøß‹/P¸þ¾ô¦ÿ—¿h!XT¶n\Å \Éÿ*¤hŠjÅ—p\ÊP0\ã›^\Ã\ì\ÞQ˜¢\Â\çV±9¹\ïUüQ°»cÁ{½<§w9ÿ2KQ(\Â\ÞÍ¢`$p½‘È£B\á6ñ\çkóRŒr©bf\ë\Ñn\ÒMÀž´`\Ø\æ8ñ\î_*Csô#ÿ‘‡\0^ŽºD\Â\í²WŠ\Å%\ÃlqsG+\"~\ÞKS\Z¯ I4Õ“Ÿ<Z\ÄG—3\ìE{ý\î!œÜ½¡û\ß\nžô\í¥ýD\\ô±½Þ\Ò=\áû­^\áŠ;¾}ôKO—¾¶\0.\Z)¬@6Þ›Ò‡ð…xq4„ô‘E\Ý[N±´«ñ\ê‘~\áz\î\Û2³B…xyBS÷=G.³ƒ‘Mð\ÚP‘®®¶ž\Î3m‚òC\nufÃ¨¹¨\ï¢÷žO¸Ã—40êš¢¸š+\è…V\à‹ª{\\ëº‡¢;„Iu¾\ì÷„\ëP,Þ–Æ‹¢S\éEˆ¾®QŠe‡µ\î¨u{Ë¯/\ßCh-µªŠ_>4u\ÙoŠ\çE_¼!c\êÕ““n\å– x”\Ëoú¯¹¶­|qhY¾¨?¥ðb4)\Î\æ\Ïø\Ð\ß3(ŒÁ²xqýØ”4ln\Öe‚ü{½y\ßt)\Æ\ÑL\äûÃ°\Îq	Q4\Ï}}óuð\ÞAoVŠñüðq\âù÷¯þvú÷9²÷Á›‰¯õ/ZñGºÔ½W\ÝYoq¼*G ¹G`™\Ë1‹\Þc\ÈU;½’™¯¼Ü³C‡:t\èÐ¡C‡:t\èÐ¡C‡:t\èÐ¡C‡ÿüH¹\Ìl!\Ùø\Ö\0\0\0\0IEND®B`‚'),('milica','2019-08-29 23:04:24',123,'jsjsjsjjs',_binary 'ÿ\Øÿ\à\0JFIF\0\0\0\0\0\0ÿ\Û\0„\0	\r\r\r(,\Z\Z%!1!%)+../\Z383-7(-1+\n\n\n\r\Z-% %/-/-------+---------------------------------------ÿÀ\0\0\Â\0ÿ\Ä\0\0\0\0\0\0\0\0\0\0\0\0\0\0ÿ\Ä\0H\0\0	\0\0\0\0!1AQa\"2Tq‘”\Ò#5Urt¡²$BR‚±³Á%3b’´\Â\Ñ4CS¢\Óÿ\Ä\0\0\0\0\0\0\0\0\0\0\0\0\0ÿ\Ä\08\0\0\0\0\0\0!1AQ\"234RSaq‘±Á#Ñ¡\áBð$rñÿ\Ú\0\0\0?\0®e²¨€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€†H`€€€€€&·@lúú\íV¡	oEðUªooFC-1\ÌzH”¹{sw|\éø%[Ä®®2—\Ð\Ù5¦\è\é.\î™ú\Êt(¾ \È\ß\ÆR\Õ\Òk\Ó>M1¢T`S\Û.\Ï\Ö>syþ{oþS\ç\Ækþ\Ì3\Ôh`´\ÆÊ®Æ´®•‡\ì\ÔN]Dd\ì–8ý$·WÑ»ñi¹…Ty²€\Ý[T¢\íNª5:ˆp\Ê\ÊU‡ªtV\îQr\ê8\ÇzT\Í<*Ž.©öù                         #Mx@²6[ªKWôûša-Q€!ˆ8.G`<\0=\ç²r\ÛwjMÁfxÿ\0\ÊV–5ò\êZó\×^+\"\"8ˆÆ½j¢i\Z$ U»¤>a\Ï_YF\î=G¨ñ\íÍ¾\Ê\ÚUb\\ˆ«\Ì\íF¿c\ÂR¢jSefVR¬„«\ÌpA\ïzEQ½¼”óûg\Ó‰\å¯agH{hh‹ª˜Ü´¸p\Ç\0‹z¥s\é\Æ$zò¬Q\çWL}cû}ø:\ç±\Ýq«—ôñ¿cr7¹bÞ£~Pg\Å9\Ø\Õy·#\ï\Û3j¸\ìc\ëQzgv¢27c+#p\çÀ\É\×M^l\ëò\Ñó4\Õ\á\Â}ü\ß$~\Ñ\Æ\êê…¸8\éªcŒ\áy±ö#eß‹+¹=–©Þ®!±”(­5T@QB¨\0\00\'˜\×\\\×3Tö¯\"˜ˆ\Ñ\Ù>_DDq\ÐS»[Ð‹B\å.©®\ï=/<tŠX\ã\évýÌ›\Öf\Õ\\\éü*³m\îÕ¬ S¢B    Jµ;Rk\é\Ò14mA\ãS/ƒ‚)Ž¿I\à;\å>\Ò\Úö°\ãv8\×\Ýý¤\ØÆª\äñä¶´&©\ØÙ\ÐÛ©qÎ£R©ý\ã\ËÕ‰\Æ\åm<œ‰Ö©\Ò;–tY·Lrf\ä\r[ˆ7v”«)J´Ò¢:+a›mÞ¹ju¢©‡\ÍTE\\\á_\ëVÌ©8j¶5S™¤\ÍóMöXùÓ‘\è\Ï\étN\åþ1\ßÚ‡{&5§‚ª¯E\é³%Edt%]Xa”Ž`‰\ØQrš¢*¦u\Õ[4\ÌO\\û|\É\É%[/úZ\Û\ì\×þCÊ»\êUýq=\"õžz¹    &\'€\í•± q\Ån”\Ö3Móü\'IÑ¹ž³T|³£\ÈSÓ¶U3ú“ ?ýÅ¢\ÙP\Z—g\È\rÜŽE‰\Û+v¦oU±5\Ç9\äßk\ÂT¿iSTUUª€*\È\ÈO:¹\\\×T\Õ3\Æy®¢\"#HsŸ“!µ=YJ\Ôú˜^\Ù3Wß¦1œ÷¨\Î=c²t{hÍ«±f¾1<¾Yvbiß…=;o‚¨€€€€€€€€€€€&ÙµeM+hX\à1¨ƒ\Òô]Wñ z\åVÚ¢jÂ¯OšN/¾g®H\ì\Þ\Ù\îqmkK†jW/ß„B?\ß:nŒÛŸ]S\Ù”ê¼˜…I;5a\ÉØ¢Ž–øãˆ§@Ž8,ù€öNW¤óüvþ©øuKZr2\\~\Òr¹þSI\Û7\Ö\íü\áª÷£–¼OKQ;-«µ7Jˆpô]c)\È>\Ñ>.Û‹”M\ÊcFbwf&ªš~ž¶J\é€þEd\ÎJ8\æq\æ;Œóm¡…V%\Ý\É\å<§½yf\äWN°\ÌHM¤5(,\ÄPKp\0$™˜¦j\ÚcV&b8Ê‚\×}a:B\íª®E\Z7n|x±EF;\'£\ì¼©b(Ÿ:x\ÏõôSd^ð•#ò\Å€€™m“iE¡|\Ô\\\án\é\î/\rõ;\Éøo\\\çúAU\Üh®?\ãûLÃ¯v¹‰\í]3…Ž<–\Ä\Ö\Ñ4š[\è\ëþU\Í\'·¦:\ËTR=€\Ë]]Üªfž\Î(ù5\Å6\çU=J@@@@@@@@@@@@@\Ìj¾±W\Ñõ\ÅZGy[µ2pŽ½ý„u©;\Þ]½\ÊøOd÷7Y½6\ê\Õy\êþŸ¶¿¥\ÒÛ¾qý\âö2ÿ\0^Fp˜WqkÝ®>½‹{wi¹\Z\Ã)!¶:®®i\ÑF«UÖ:cyÙŽó>\íZª\íQE¬\Ïc1¬©\Ý}×¦½Íµ¶R\×>;qWDg‚r\á\Ì\ãd\íöNÇŒ\ä»\çww*òrwüšy òýH`€€õ‚8*C)Á \ÌM11¤ñf&bu…·¨\ÛAJÊ¶÷\ÕWZu[‚T[\Çõ_\Øt\ã6¶Äª‰›¶#‡lw|–xùQ>MK?)\Í\ÌLv\'GO³§ôýµ…#R\â 	¦ƒ£‘Ô‹ýy	/öU{¶\ã‡c]Û´ÛfT~¶k%]#\\\Õšø´i\ïª£·µYÿ\0‰\ß\àlú1-\îG\í•E\ë\Ór­XI= €†H`€€€€€€€€€€‡gôê¶“µ]\ï“P©\ÇÍ¨,\àö‚1\Þ%f×š)Ä®kt\åóH\Æ\×\ÂF‹úy\Ï%\Ñµ]Z\â\È=\ä[?IV˜<qÅ±\ÖWž=2÷`dÛµv¾\Þ=È™tU4pR³¼Th@@@@@@@˜\ì\ê\çH½\Ý*VÕªô\Ê\×\nX½¦Tžñ\0ú8Q\í›X”Xš\îS\Ó\Ê{e/\ZnU_>ºpKr^ô[Mq^ƒn\Õ^Q°\îýUB@=`1\ç,¶N=7ò©¢¾_\ÓFEsM¹˜P·wU+9©V£Ô¨\Ü\ÙØ³Yž‡nÍ»t\î\Ñ\ZBšj™\æ\é›$2C!’      X{³\rss\\ƒó4Všœf£dñ\í\Â~3š\é5\Ý\Û\Ñ\ß:ý“ðiÖ©•¹8µ‘†>B’\Ú6ª*\Ý=ý\áŽ1Ê›ž%`<Ç Ž©\Þl]¥6÷*ó£üª2l\îN±\É\r—¼ùrD     euo@W\Ò\Å\Z#\0`\Õr<Jk\Ú\Ýýƒ®C\ÍÎ·‹o~¿¤w¶Úµ7\'H_\Z¿¡(X\ÐZ\0qv>[·[1\íþ\Ï32\îe\\šëŸ§r\æÝ¸¢4†JEl E6¥ôE\ÏÚ¶ÿ\0SN\\l]§ê—\è”\\ô1\ìÎ¤0@@@@@@¶¶-Lk·\ëk…SÙ…¦ü\Æq\'«ùh‡\ígL\ÊÅœ\ÊyÉ¥tu+ª5-\ë.õ:«†\ê#°ƒ\ÔA\ã7c\ä\\Ç¹h\çŠ\èŠ\ãIkö±hJ¶oWŽ4\Øc™Â¸\áœr<§¤a\æ[Éµ(ŸŸ\ÍIv\ÜÛ«Ic$¶²d&kVuf\çH\ÔÜ¢7i©ùÚ¬§£N\ìõ·$~Œ´mbQ­sÇ²­Yª\äð^z¿¡(X\ÐZ\0qv8\ßv\ëf=¿\Âp™—2®Mw\'ý.-[‹q¤2R#a=´\Z;ú.ôn\ïn\Ò	âŽ¬«õK-‘V™”|\Úr#ø\å@\ÏGQ\"\æ\Øò£Ü€2\×U7Y\Â „\é\ÏY¦>¹[ayŸT\æP&#úë««¤-Zž>~˜/l\Ù\Æ?²ye²óªÄ»lóh¿j.SñPu©23#©WF*\êF \àƒ=Š\é®\"ºyJ–cI\Ò\\\'\Ó3£9ª:·WH\×\×+E71Á°g›@zù	]´s\èÄµ½<\ç”wÿ\0¦û¦\ä\éØ¾tfŽ¥kI(P@”\éŒ(‰\'¬“Ä“<öýú\ïÜ›—\'Y•\Å\Å\éT\Òúp£Y\\eXdŒ«duƒ>\ë·]¥Q£1<œ\ç\Ã$·\ém.©[¤·¬¸\æ™\0	#©¦õG{\â\äkD\Ã[Dõ\ì2Cc•³aU1ý\Ý\Óñ\íÞ¦†pý$§Lšg\áû•¶\ëDü\Ó\É\Ï&ñ®\Õ5O|6 ¾:òµ\ÊP0*u€8÷\Ù:ƒ´÷f1\îO\Ï\é.Æ¾\\*©\Ø+Y½TÕº\ÚF¿GOÅ¦˜5\ê•A\Ù\ÞÇ¨Ä¯\ÏÏ·‰oz®3<£¿ý7Y³7gN\Å\í¡´M:)B‚n¢s\ëf=lÇ­Œóì¬«™7&»“¬þQS¤=7W4\é#Tª\ê”\é‚\Î\Ì@PY3U»u\\«v˜\ÖYª¨¦5•G®»B©pZ…“5+]\Ç\n•G.h¾\Â{¹N\ÏflJ,\Ä\\½\Z\Õ\ÝÜ­¿•5N\í<™\í‹S\"\Ò\é¸n›  w­\'‡¡—\Ù+ºM4øj\"#±»]É™XsšN qu\Þyo=£\ê\Ü\é]3ñý±<´k%T\Ýf^{¬\Ë\ì8ž©nu¢\'à «œ¸Ï·\ÉÁ\ÙØµ\\\Û]¦8­Â¾~\Õ0?\Ûø\Î7¤ô%|?k<òecNa<€\Ú­m£n*\ÐsN 40\æ\ÕTlv\ÆZlk^Ì¦›‘¬qü4dW4[™†e\Ú\Ô\×(Ö—5K\ÜS%è³¶]\Ðñ#\'\Êe9õ\éa·6lZ˜½j#N1\Ý-8—¦¯&©âŸ°`€A\æ\È>™\Í\Ó3\ÎV–\Ù}V½?\'tK:§$\ê\\|dú\ß\á\ê\ÇŒq\ë\ìtŠ˜Ç	\Z\×>}xZ\×Ã’\È\Ð\Ú*¡A7Q=lÇ­˜õ±\íœ\ÆVUÌ›“r\ä\ë?÷‚u\Å¤<ZË­º=3YóQ†i\Ò\\\Z­\ê\ê\ç„Ýƒ³oeÏ“;ûoSn8©iÖ»\"ÿ\08w(©\Í**N\à\ì-ûm\Þ}@N\ëf\ÙÄ¦4g¶{UWo\ÕrXc=òÐºvCD.,9Ô¹ª\ÏÇ¬AR‰\ÂôŠ¹œ½;¢#ö·Ã-ýSi@–@L\Ä\è5¯LR	sr‹Ô¸¬«““Q€\Ìõ,i\Ö\ÍðÃŸ¯ÎŸ›\É7>Hv\Å*œ\ß\'\êAùq\É\éôœ§J(\Ö-\Õóý,0;ah\ÎEd@@‰mOè›·oþ¡%\ÎÀõ\ê~¿„\\\ÏC*B…f¦\Ê\è\Åd`pÀŽD\ßWE5Ó¥P©‰˜ao\ê>\Ð\ëv\Þð¥;Ž‚Ó«\Ø?\ÂýÜWd\âö®Äª\Ì\Í\Ûi\îí…ž>V÷“W4\æ\æ\á)#T¨\ê”\Ðe™˜*\ÞL\ç\è·]un\Ó2™5Dq•g­;O9z:=F\Ý\éÛˆ<8šhG°·²uX\"\æDý÷³g•*\Ò\æ\á\ê»T¨\ìõ\åÙ˜³\ÞL\ê-Û¦\Ý1M0US3¬ñuÍ’\ç²Áý“lp2^\äžÿ\0I¨8û\'Ÿmÿ\0^ª;´ü.q=%’$€˜‘®:\ËH¥õ\â·1u_<sÎ¡?\ÖzŽQV=Ð¡»\ZW,t’\Ö@@@@@@@@@@@@@@@Ÿ\ìj°µÓŽj[;<J‹œÿ\0šs%£\\zj\îŸ\Ïÿ\0°gJ\åpN!hL„žÔ¾‰¸ûvÿ\0\ÏIs°=vŸ¯\á3\ÐÊŒžØ¨’%‡¦\ãHW¨ª•+Õ¨‰\ä+UvQ\Ã\0™¦Œ{TN´Sû›•Ok\Í7hø   _»=@º.\È\0i8\ígbO¬’gœm‰™Í¹3ðü.ñ½$Rµ¼€˜cµ¯:\çô•÷Þªþi\é»7\Õmü”wý$°\ÒkQ[²»\Í)DGKNµ?O‰¾ÿ\0&}R›oÑ½…T÷LO\ëö“‡:]]w7”©*Ó¦j¶\í0ÎªX\ã8\\ó3ƒ¢\Í\ÊõÜ¦gN\å¼\ÕLs—|\Öú Dö§ôM\ÇÛ·þzKƒ\ë´ýÙž†Tdô4ó     &FÀj#E\Ùdc\æö’Dóm­19—4\ï]\ãz*Yù]ðo &Ö¼kŸ\ÒWÿ\0z«ù§¦\ì\ßU·òQ_ô’\ÃÉ­DÎ¦\\tZF\Éøð¸E8\Æpþ!ûH;N\Þþ%tü?[¬N—!bm‡Fo[Ð¼NkSp‘œ\î\Ô#\Ô\Ê=³—\è\îDEÊ­Ly\Ñøÿ\0Iù”Î›ñØ•j–—¶Tk\à`V 8e8?\Ã>¹U´±g&«_¤¤Y¯~ˆ©˜[Q]¨S-¢np3† \Ç\Ð+¡&\\l\Z¢3¨\×\ãøF\Ëô2¢§ ©\ä†	‘°úž³l>\çoü¥že´}j\ïþ\Óù^Xôtüœµ¯L|†Îµ\ÈP\ÍL(¦pY˜*\ç\\c­_¦\Ïg9–oW¹Fó£R´½[\Û*w5‘QÝª0RÊƒƒ\Ë8Ÿ{W\Þ6EV\èX±rnQ«;+›»Zó®_I_ý\ê¯æž›³}V\ß\ÉE\ÒK\r&µ\É2:¹Ižö\ÑP\Æ\æŽ\é\0<pI\ÆEÍ˜‹\Ì÷O\á²\Ôk\\/ý?£…Õ­Å¹ÿ\0½I•{›S\ê \ç8w\æ\ÍúnGz\ê\í\Ô\ÌJ¿\ØÆ‘#\åVlpWv½5\ë©W\Øw=³¢\é%˜˜¢ü|§ô‡…^š\Ñ+>r%ƒ®½6¼¦K[\Ô+\Ï\ÊU\Þ^]\àI\Û:\ï‚É¢¿Œ5^m\Ë^\'¦i¢‹B!‚\0)<xI\å>j«Hf#V\ÌX\Ð\è\éR§ÿ\0Žš\',y*/Tò\Ûõ\ïÝª®ù™_\Ñ´\Ä »f¼Ý´·¢÷\Õ\Ë|©¡þ®¼ÿ\0¤¾\èÕ­\ë\Õ\Ü\î3jÒ˜†of\ßEYýšŸ\Îynzõ\Ïû\ØÛ‹\è©I¥JGk^5\Ï\é+\ï½Uü\Ó\Óvoª\Ûù(¯úIa\äÖ¢u¥Z\Î)Ñ¦õ*7’¨¥›\Ø:»æ»—hµ\Õ\ÌD|_T\Ó5N‘[gš‰RÖ ¼¼À¬ Š\Ã\Ü\Þ,\ä~¶	“Ï«\Ûf›ôø:\é\Û?¨X\ãcn\ÎõKs0Ÿ¢ \Ñ?¡k+\Ó*U¯Y;Š\ÖMõ\Æz··G«µ\Èÿ\0\Ê\Ù_tGøà«£\È\È\Ño\Î)hø@<\È<\îë™‰\Òa‰\äÖ­\'i\ÐW¯G\ÌV©LgÂ¹8\îÔ±\îø[t\×\ß\Z¨k*—šn|3š“£>U¤-©c*µZ¼´ücœö\à\\¯Ú™º»t\Ò>rßFýÈ†Á\Ï6]©Í±^\ï\ßR¢1‹{pOÚ¨Äœú•goÑ»[¸\Ó_µ?…VuZ×»ÜœlÂ¶öŠ·\á\ÃU\çXç»Ÿ.\éA·i\ÝÎ«\é?¤\ÌI\Ö\Õ)\\¥„ŽÖ¼\ëŸ\ÒWÿ\0z«ù§§l\ßU·òQ\ßô’\ÃI­D	.¨k…MµV½:¦³)%™”ÑŒ\\e^\Ñ\Ùt\æ\ÕL\Õ\\\ÄGÃ½\"\Íù·\ÃVr¾\Ö.\Èù»[u9\âYª¸ö²ºŽŒÙŽu\Ìÿ\0†\éÎ®c”=\Ú3k9e[«L/\ë=*™#¿£n¯\Þö\È\Ù\Zˆ‰›Uq\î–\Ê3½¨au»N\ÛWÒ¶—vµK\"|˜T&›®\éJÄŸ€ÏŠ{\å†\ëX7,]<\í>\Í7nSUØª•\Õ8I\ç+bf9q\ÖJÂ¥\í\åEò^\ê»/.F£c”ô\ì\Z&Œkt\ÏdD…\r\ÙÖº˜\é)¬€€€p\ì£WM½¼ª1R\íGF?f—0O{>€³ˆ\ét^¹¨žóù­p\ì\î\Æôó”ús©­|×‹Î›I^>rcIyð€§Ž=\ê}³\Ò6]¯‡E?&E[\×%`ljôµµ\Å\ÄôUpÀZ€òý\åc\ëœ\ïI¬\îÝ¢\äG>	¸5y;«s\Å9¯úûjô´\àqúÆªs\â¯\ã)\Ã\Òô“v›˜”LvB“&™¦\ä°É €€€€€€€iø#O?ou\ä|gŸwuPióÁ\Zyû{ªüq\ã<û¸ûB=£Á\Zyû{ªüq\ã<û¸ûB=§\ßi\ç\í\î«ñÇŒó\î\ã\îuöiõƒ{ªüq\ã<û¸ûF=£Á\Z}`\Þ\ê¿Ç\î\ã\îuöi\ç\í\î«ñ\Ìø\ÑW»¹\Ô#\Úü\Ó\Ï\ß\ÝG\Ç1\ãDû¸ûB=¯Á\à>°ou_Ž<gŸus¨G´ûOd¨?/núU\êýù‰\é,\ÕO‚\ç\Ý3ý>£\"u\ÞYs–™\ÖfS¹pyt½J´jS¥W¡zŠT>\æùPxGr=Sv=\ÊmÜŠ\ê§];5ÑŠ¢f4‰\Ñ^\r‘\'Ÿ·ºŽtqÒ‰\ìµt£µ>ø#O¬\ÝG\Ç3\ãDû¸ûF=¯Á\à<ý½\Õ~9Ÿ\ç\Ý\Ç\Ü\ê\í\Ó\Ï\Û\ÝW\ã\ç\Ý\Ç\Ü\ê\í\Ó\Ï\Û\ÝW\ã\Z\'\Ý\ÇÝž¡\ÒK¢õF\ÐD\rl•ª&	z€±f\ÇºN\0\î\ê•7ö\Ö]Ù™Š\æ#º4H£\Z\Ý0“*§op¬«`®A\n\ÅwÀ=D®F}ŸTM:\ÅUqˆ\ì&5…q[d\áÙ´ƒ–vfcòU\âX\äŸ/´Îžž“n\ÓÅ¨\áñAœ™\×y\Ð?©aXW¡¤Hlnºµ (ËHa\ÒwsD•·(Ê·»]¨\Ó\ç\É÷oÁÎ±Rr \ãŽ3×\ìœüü\Ñ]rÔ¤\Òu)T5\Í¤Œ‡EBÀœŒ\áË´Ë›µ\êÂ¦iˆ\×^\ÍQ¯\ãøYŽ(÷‚4óö÷Uøå—\î¿\ËGQhðFŸX?ºŽ<hŸws¨Çµø<§\Ö\r\î£\ã™ñž}\Ü}Î¡\Ñ\à<ý½\Õ~8ñž}\Ü}\Ù\ê\í\Ó\ë÷Uø\æ<hŸwv:„{G‚4óö÷Uø\æ|hŸws¨Ç´x#O?ou_Ž<hŸws¨G´x#O¬\ÝW\ã\Z\'\Ý\ÇÝž¡\Ñ\à<ýý\Ô|s4O»»F=¯\ÂÌœªÄ€€€€€€€€€€€€€€€€€€€€Ž\ÝBÿ\Ù');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `idusers` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`idusers`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'bakir','car'),(3,'amra','carica'),(5,'milica','carica'),(8,'nemanja','car'),(12,'s','bakir'),(13,'bbbb','123'),(14,'q','3333'),(41,'tiki','car'),(42,'r','r'),(43,'riki','r');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-30  1:06:31

Vim�UnDo� ��Y�RD�Ri�ǉf��f�T^��u��$i�*\                  hue += 2            F       F   F   F    Mӧ�    _�                     
   
    ����                                                                                                                                                                                                                                                                                                                                                             MӞ�     �   
          5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Mӟ     �   
                    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Mӟ[    �                               "PNG"5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Mӟ�    �                 generate_tiles(100)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Mӟ�     �                   saturation = 05�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Mӟ�     �                   saturation = 55�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Mӟ�     �                   saturation = 505�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             Mӟ�    �                   lightness = 05�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             Mӟ�     �                           lightness += 15�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             Mӟ�     �                           hue += 15�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             Mӟ�    �                       saturation += 15�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             Mӡ    �   	            J                "hsl({0}, {1}%, {2}%)".format(hue, saturation, lightness))5�_�                   
       ����                                                                                                                                                                                                                                                                                                                                                             MӢ�     �   	   
          K                ("hsl({0}, {1}%, {2}%)".format(hue, saturation, lightness))5�_�                    	   )    ����                                                                                                                                                                                                                                                                                                                                                             MӢ�     �      
         )        tile = Image.new("RGBA", (8, 8), 5�_�                    	   )    ����                                                                                                                                                                                                                                                                                                                                                             MӢ�     �      
         *        tile = Image.new("RGBA", (8, 8), )5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             MӢ�     �      
                 �      
       5�_�                   	       ����                                                                                                                                                                                                                                                                                                                                                             Mӣ]    �               O        colour = getrgb("hsl({0}, {1}, {2})".format(hue, saturation, lightness)5�_�                    
   G    ����                                                                                                                                                                                                                                                                                                                                                             Mӣd   	 �   	            G                "hsl({0}, {1}, {2})".format(hue, saturation, lightness)5�_�                       L    ����                                                                                                                                                                                                                                                                                                                                                             Mӣq   
 �               M        tile.save("tile-{0}-{1}-{2}.png".format(hue, saturation, lightness), 5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             Mӣ�     �      
                 colour = getrgb(5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Mӣ�     �               import ImageDraw5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Mӣ�    �               import Image5�_�      !               
       ����                                                                                                                                                                                                                                                                                                                                                             Mӣ�     �   	            H                "hsl({0}, {1}, {2})".format(hue, saturation, lightness))5�_�       "           !   
   #    ����                                                                                                                                                                                                                                                                                                                                                             Mӣ�    �   	            I                "hsl({0}, {1}%, {2})".format(hue, saturation, lightness))5�_�   !   #           "   
   I    ����                                                                                                                                                                                                                                                                                                                                                             Mӣ�     �   
          5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                             Mӣ�     �   
                    5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                             MӤ�     �   
                     5�_�   $   &           %   
   J    ����                                                                                                                                                                                                                                                                                                                                                             MӤ�     �   	            J                "hsl({0}, {1}%, {2}%)".format(hue, saturation, lightness))5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                             MӤ�    �      	             �      	       5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                                                             MӤ�     �                                alpha5�_�   '   )           (   
       ����                                                                                                                                                                                                                                                                                                                                                             MӤ�    �   	            #        colour = ImageColor.getrgb(5�_�   (   *           )   
       ����                                                                                                                                                                                                                                                                                                                                                             MӤ�     �   	            $        colour = (ImageColor.getrgb(5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                                                             MӤ�     �                                alpha)5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                                                             Mӥ     �                                 alpha5�_�   +   -           ,      J    ����                                                                                                                                                                                                                                                                                                                                                             Mӥ    �   
            K                "hsl({0}, {1}%, {2}%)".format(hue, saturation, lightness)),5�_�   ,   .           -      /    ����                                                                                                                                                                                                                                                                                                                                                             Mӥ     �             5�_�   -   1           .          ����                                                                                                                                                                                                                                                                                                                                                             Mӥ    �                       5�_�   .   2   0       1      0    ����                                                                                                                                                                                                                                                                                                                                                             Mӥe     �               L        tile.save("tile-{0}-{1}-{2}.png".format(hue, saturation, lightness),5�_�   1   3           2          ����                                                                                                                                                                                                                                                                                                                                                             Mӥh     �               (            hue, saturation, lightness),                   "PNG")5�_�   2   4           3      #    ����                                                                                                                                                                                                                                                                                                                                                             Mӥl     �               0        tile.save("tile-{0}-{1}-{2}.png".format(5�_�   3   5           4      &    ����                                                                                                                                                                                                                                                                                                                                                             Mӥo    �               /            hue, saturation, lightness), "PNG")5�_�   4   6           5          ����                                                                                                                                                                                                                                                                                                                                                             Mӥs     �             5�_�   5   7           6          ����                                                                                                                                                                                                                                                                                                                                                             Mӥs     �                       5�_�   6   8           7          ����                                                                                                                                                                                                                                                                                                                                                             Mӥx     �                       �             5�_�   7   9           8          ����                                                                                                                                                                                                                                                                                                                                                             Mӥ�    �                       saturation += 25�_�   8   :           9          ����                                                                                                                                                                                                                                                                                                                                                             Mӥ�     �             5�_�   9   ;           :          ����                                                                                                                                                                                                                                                                                                                                                             Mӥ�    �                       5�_�   :   <           ;          ����                                                                                                                                                                                                                                                                                                                                                             Mӥ�    �                   saturation = 05�_�   ;   =           <          ����                                                                                                                                                                                                                                                                                                                                                             Mӥ�    �                       alpha += 205�_�   <   >           =          ����                                                                                                                                                                                                                                                                                                                                                             MӦ�     �                           saturation += 25�_�   =   ?           >          ����                                                                                                                                                                                                                                                                                                                                                             MӦ�    �                           lightness += 25�_�   >   @           ?          ����                                                                                                                                                                                                                                                                                                                                                             MӦ�    �                           hue += 25�_�   ?   A           @          ����                                                                                                                                                                                                                                                                                                                                                             Mӧ     �                           hue += 45�_�   @   B           A           ����                                                                                                                                                                                                                                                                                                                                                             Mӧ�     �                            saturation += 205�_�   A   C           B           ����                                                                                                                                                                                                                                                                                                                                                             Mӧ�     �                        if saturation > 100:5�_�   B   D           C           ����                                                                                                                                                                                                                                                                                                                                                             Mӧ�     �                            saturation = 05�_�   C   E           D           ����                                                                                                                                                                                                                                                                                                                                                             Mӧ�     �                            lightness += 205�_�   D   F           E           ����                                                                                                                                                                                                                                                                                                                                                             Mӧ�     �                        if lightness > 100:5�_�   E               F           ����                                                                                                                                                                                                                                                                                                                                                             Mӧ�    �                            lightness = 05�_�   .       /   1   0      (    ����                                                                                                                                                                                                                                                                                                                                                             Mӥa     �               (        tile.save("tile-{0}-{1}-{2}.png"   4                .format(hue, saturation, lightness),5�_�   .           0   /      0    ����                                                                                                                                                                                                                                                                                                                                                             Mӥ\     �               0        tile.save("tile-{0}-{1}-{2}.png".format(   (            hue, saturation, lightness),5�_�                    	   4    ����                                                                                                                                                                                                                                                                                                                                                             Mӣ     �      
         4        colour = getrgb("hsl({0}, {1}, {2})".format(   3                        hue, saturation, lightness)5�_�                   
   J    ����                                                                                                                                                                                                                                                                                                                                                             Mӡ     �   	            J                ("hsl({0}, {1}%, {2}%)".format(hue, saturation, lightness)                       )5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Mӡ    �   
                            , alpha) )5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Mӡ2     �                   5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Mӡ2     �      	             alpha = 05�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Mӡ@     �                       �                       if alpha > 100:5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             MӡF     �                           saturation += 25�_�                           ����                                                                                                                                                                                                                                                                                                                                                             MӡI     �                           �                           alpha = 05�_�                            ����                                                                                                                                                                                                                                                                                                                                                             MӡL    �                       �                       alpha += 205��
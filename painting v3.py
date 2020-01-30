import pygame
pygame.init()
safhenamayesh=pygame.display.set_mode((1000,600))
pygame.display.set_caption("paint")
safhenamayesh.fill((245,245,245))

done=False
clock=pygame.time.Clock()

the_shape=""
the_color=(0,0,0)
the_size=""
size=5
the_surf=""
surf=0



 #کادر اشکال
pygame.draw.line(safhenamayesh,(0,0,0),(2,2),(2,402))
pygame.draw.line(safhenamayesh,(0,0,0),(2,2),(102,2))
pygame.draw.line(safhenamayesh,(0,0,0),(102,2),(102,402))
pygame.draw.line(safhenamayesh,(0,0,0),(2,402),(102,402))
pygame.draw.line(safhenamayesh,(0,0,0),(2,412),(102,412))
        #اشکال
        #rect
pygame.draw.line(safhenamayesh,(0,0,0),(12,12),(92,12))
pygame.draw.line(safhenamayesh,(0,0,0),(92,12),(92,62))
pygame.draw.line(safhenamayesh,(0,0,0),(92,62),(12,62))
pygame.draw.line(safhenamayesh,(0,0,0),(12,62),(12,12))

pygame.draw.line(safhenamayesh,(0,0,0),(2,102),(102,102))
        #cir
pygame.draw.circle(safhenamayesh,(0,0,0),(52,142),35,1)

pygame.draw.line(safhenamayesh,(0,0,0),(2,202),(102,202))

        #tri
pygame.draw.polygon(safhenamayesh,(0,0,0),[(52,212),(12,272),(92,272)],1)

pygame.draw.line(safhenamayesh,(0,0,0),(2,302),(102,302))

        #line

pygame.draw.line(safhenamayesh,(0,0,0),(12,352),(92,352))

        #کادر رنگ
pygame.draw.line(safhenamayesh,(0,0,0),(2,412),(2,592))
pygame.draw.line(safhenamayesh,(0,0,0),(2,412),(102,412))
pygame.draw.line(safhenamayesh,(0,0,0),(2,592),(102,592))
pygame.draw.line(safhenamayesh,(0,0,0),(102,592),(102,412))
        #رنگها
pygame.draw.rect(safhenamayesh,(0,0,0),(2,412,50,30))
pygame.draw.rect(safhenamayesh,(40,40,40),(52,412,50,30))
pygame.draw.rect(safhenamayesh,(128,128,128),(2,442,50,30))
pygame.draw.rect(safhenamayesh,(112,128,144),(52,442,50,30))
pygame.draw.rect(safhenamayesh,(119,136,153),(2,472,50,30))
pygame.draw.rect(safhenamayesh,(70,130,180),(52,472,50,30))
pygame.draw.rect(safhenamayesh,(30,144,255),(2,502,50,30))
pygame.draw.rect(safhenamayesh,(0,191,255),(52,502,50,30))
pygame.draw.rect(safhenamayesh,(220,20,60),(2,532,50,30))
pygame.draw.rect(safhenamayesh,(165,42,42),(52,532,50,30))
pygame.draw.rect(safhenamayesh,(220,20,147),(2,562,50,30))
pygame.draw.rect(safhenamayesh,(255,105,180),(52,562,50,30))

#کادر اضافس
pygame.draw.rect(safhenamayesh,(0,0,0),(102,2,40,40),1)
medad=pygame.image.load("c:/medad barnamam.png")
safhenamayesh.blit(medad,(102,2))
pygame.draw.rect(safhenamayesh,(119,136,153),(102,42,40,40),2)
pygame.draw.rect(safhenamayesh,(119,136,153),(102,82,40,40),2)
pygame.draw.rect(safhenamayesh,(119,136,153),(102,122,40,40),2)
plus=pygame.image.load("c:/plus.jpg")
safhenamayesh.blit(plus,(102,42))
minus=pygame.image.load("c:/minus.png")
safhenamayesh.blit(minus,(102,82))
eraser=pygame.image.load("c:/eraser_PNG32.png")
safhenamayesh.blit(eraser,(102,122))
surface_maximize=pygame.image.load("c:\\surface_maximize.png")
safhenamayesh.blit(surface_maximize,(102,162))
surface_minimize=pygame.image.load("c:\\surface_minimize.png")
safhenamayesh.blit(surface_minimize,(102,202))
clear=pygame.image.load("c:\\clear.png")
safhenamayesh.blit(clear,(102,242))





while not done:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            raise SystemExit(0)



        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y=pygame.mouse.get_pos()
                if(2<x<102 and 2<y<102):
                    the_shape="rect"
                elif(2<x<102 and 102<y<202):
                    the_shape="cir"
                elif(2<x<102 and 202<y<302):
                    the_shape="triangle"
                elif(2<x<102 and 302<y<402):
                    the_shape="line"
                elif(102<x<142 and 2<y<42):
                    the_shape="azad"
                elif(102<x<142 and 42<y<82):
                    size+=1
                elif(102<x<142 and 82<y<122):
                    size-=1
                elif(102<x<142 and 162<y<202):
                    surf+=1
                elif(102<x<142 and 202<y<242):
                    surf-=1

                elif(102<x<142 and 242<y<282):
                    the_shape="clear"

                elif(102<x<142 and 122<y<162):
                    the_shape="eraser"

                elif(2<x<52 and 412<y<442):
                    the_color=(0,0,0)
                elif(52<x<102 and 412<y<442):
                    the_color=(40,40,40)
                elif(2<x<y and 442<y<472):
                    the_color=(128,128,128)
                elif(52<x<102 and 442<y<472):
                    the_color=(112,128,144)
                elif(2<x<52 and 472<y<502):
                    the_color=(119,136,153)
                elif(52<x<102 and 472<y<502):
                    the_color=(70,130,180)
                elif(2<x<52 and 502<y<532):
                    the_color=(30,144,255)
                elif(52<x<102 and 502<y<532):
                    the_color=(0,191,255)
                elif(2<x<52 and 532<y<562):
                    the_color=(220,20,60)
                elif(52<x<102 and 532<y<562):
                    the_color=(165,42,42)
                elif(2<x<52 and 562<y<592):
                    the_color=(220,20,147)
                elif(52<x<102 and 562<y<592):
                    the_color=(255,105,180)

    if(the_shape=="rect"):
        pygame.event.poll()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                i,j=pygame.mouse.get_pos()
                if(i>142):
                    pygame.draw.rect(safhenamayesh,the_color,(i,j,75+surf,45+surf),size)

    if(the_shape=="cir"):
        pygame.event.poll()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                i,j=pygame.mouse.get_pos()
                if(i>142):
                    pygame.draw.circle(safhenamayesh,the_color,(i,j),30+surf,size)

    if(the_shape=="triangle"):
        pygame.event.poll()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                i,j=pygame.mouse.get_pos()
                if(i>142):
                    pygame.draw.polygon(safhenamayesh,the_color,[(i,j),(i+40,j+60),(i-40,j+60)],size)

    if(the_shape=="line"):
        pygame.event.poll()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                i,j=pygame.mouse.get_pos()
        pygame.event.poll()
        if event.type==pygame.MOUSEBUTTONUP:
            if event.button == 1:
                l,k=pygame.mouse.get_pos()
                if(i>142 and l>142):
                    pygame.draw.line(safhenamayesh,the_color,(i,j),(l,k),size)

    if(the_shape=="azad"):
        pygame.event.poll()
        if event.type==pygame.MOUSEMOTION:
           endpos=pygame.mouse.get_pos()
           if pygame.mouse.get_pressed()==(1,0,0):
                if(endpos[0]>142):
                    pygame.draw.line(safhenamayesh,the_color,startpos,endpos,size)
           startpos=endpos

    if(the_shape=="eraser"):
        pygame.event.poll()
        if event.type==pygame.MOUSEMOTION:
           endpos1=pygame.mouse.get_pos()
           if pygame.mouse.get_pressed()==(1,0,0):
                if(endpos1[0]>142):
                    pygame.draw.line(safhenamayesh,(245,245,245),startpos1,endpos1,size)
           startpos1=endpos1



    if(the_shape=="clear"):
        safhenamayesh.fill((245,245,245))
         #کادر اشکال
        pygame.draw.line(safhenamayesh,(0,0,0),(2,2),(2,402))
        pygame.draw.line(safhenamayesh,(0,0,0),(2,2),(102,2))
        pygame.draw.line(safhenamayesh,(0,0,0),(102,2),(102,402))
        pygame.draw.line(safhenamayesh,(0,0,0),(2,402),(102,402))
        pygame.draw.line(safhenamayesh,(0,0,0),(2,412),(102,412))
                #اشکال
                #rect
        pygame.draw.line(safhenamayesh,(0,0,0),(12,12),(92,12))
        pygame.draw.line(safhenamayesh,(0,0,0),(92,12),(92,62))
        pygame.draw.line(safhenamayesh,(0,0,0),(92,62),(12,62))
        pygame.draw.line(safhenamayesh,(0,0,0),(12,62),(12,12))

        pygame.draw.line(safhenamayesh,(0,0,0),(2,102),(102,102))
                #cir
        pygame.draw.circle(safhenamayesh,(0,0,0),(52,142),35,1)

        pygame.draw.line(safhenamayesh,(0,0,0),(2,202),(102,202))

                #tri
        pygame.draw.polygon(safhenamayesh,(0,0,0),[(52,212),(12,272),(92,272)],1)

        pygame.draw.line(safhenamayesh,(0,0,0),(2,302),(102,302))

                #line

        pygame.draw.line(safhenamayesh,(0,0,0),(12,352),(92,352))

                #کادر رنگ
        pygame.draw.line(safhenamayesh,(0,0,0),(2,412),(2,592))
        pygame.draw.line(safhenamayesh,(0,0,0),(2,412),(102,412))
        pygame.draw.line(safhenamayesh,(0,0,0),(2,592),(102,592))
        pygame.draw.line(safhenamayesh,(0,0,0),(102,592),(102,412))
                #رنگها
        pygame.draw.rect(safhenamayesh,(0,0,0),(2,412,50,30))
        pygame.draw.rect(safhenamayesh,(40,40,40),(52,412,50,30))
        pygame.draw.rect(safhenamayesh,(128,128,128),(2,442,50,30))
        pygame.draw.rect(safhenamayesh,(112,128,144),(52,442,50,30))
        pygame.draw.rect(safhenamayesh,(119,136,153),(2,472,50,30))
        pygame.draw.rect(safhenamayesh,(70,130,180),(52,472,50,30))
        pygame.draw.rect(safhenamayesh,(30,144,255),(2,502,50,30))
        pygame.draw.rect(safhenamayesh,(0,191,255),(52,502,50,30))
        pygame.draw.rect(safhenamayesh,(220,20,60),(2,532,50,30))
        pygame.draw.rect(safhenamayesh,(165,42,42),(52,532,50,30))
        pygame.draw.rect(safhenamayesh,(220,20,147),(2,562,50,30))
        pygame.draw.rect(safhenamayesh,(255,105,180),(52,562,50,30))

        #کادر اضافس
        pygame.draw.rect(safhenamayesh,(0,0,0),(102,2,40,40),1)
        medad=pygame.image.load("c:/medad barnamam.png")
        safhenamayesh.blit(medad,(102,2))
        pygame.draw.rect(safhenamayesh,(119,136,153),(102,42,40,40),2)
        pygame.draw.rect(safhenamayesh,(119,136,153),(102,82,40,40),2)
        pygame.draw.rect(safhenamayesh,(119,136,153),(102,122,40,40),2)
        plus=pygame.image.load("c:/plus.jpg")
        safhenamayesh.blit(plus,(102,42))
        minus=pygame.image.load("c:/minus.png")
        safhenamayesh.blit(minus,(102,82))
        eraser=pygame.image.load("c:/eraser_PNG32.png")
        safhenamayesh.blit(eraser,(102,122))
        surface_maximize=pygame.image.load("c:\\surface_maximize.png")
        safhenamayesh.blit(surface_maximize,(102,162))
        surface_minimize=pygame.image.load("c:\\surface_minimize.png")
        safhenamayesh.blit(surface_minimize,(102,202))
        clear=pygame.image.load("c:\\clear.png")
        safhenamayesh.blit(clear,(102,242))











    pygame.display.flip()
    clock.tick(120)
quit()


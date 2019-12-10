import matplotlib.pyplot as plt
import numpy as np

ten = [ 5.575145244598389, 5.132342815399170, 4.889571666717529, 4.567566871643066,
        4.649691104888916, 4.458029270172119, 4.389657020568848, 4.349104404449463,
        4.253368854522705, 4.293147087097168, 4.1898393630981445, 4.347694396972656,
        4.3503737449646, 4.039025783538818, 4.220725059509277, 3.9929096698760986,
        4.123685359954834, 3.9230425357818604, 3.938328981399536, 4.045256614685059]

ten_two = [5.594398498535156, 5.0131072998046875, 4.988063335418701, 4.624997615814209,
           4.624422550201416, 4.318336009979248, 4.544387340545654, 4.181450843811035,
           4.43215799331665, 4.150700569152832, 4.116442680358887, 4.1857380867004395,
           4.231636047363281, 4.009681701660156, 3.997680902481079, 4.064757823944092,
           4.014954566955566, 3.910567283630371, 4.009210109710693, 3.918236255645752,
           4.224245548248291, 3.975353479385376, 3.867281436920166, 3.8477840423583984,
           3.847684621810913, 3.856177806854248, 3.760077476501465, 3.756516456604004,
           4.0319719314575195, 3.6944165229797363, 3.8551037311553955, 3.762603282928467]

twenty = [5.184959888458252, 4.50337028503418, 4.599796295166016, 4.334005832672119,
          4.195288181304932, 4.124048233032227, 4.23002815246582, 4.206910610198975,
          3.997889280319214, 3.9738574028015137, 3.959397792816162, 3.961040496826172,
          4.3617448806762695, 3.933809757232666, 4.065454959869385, 3.743276357650757,
          3.820070743560791, 4.012623310089111, 3.779560089111328, 3.6953015327453613]

thirty = [5.106256008148193, 4.404909133911133, 4.321137428283691, 4.090065956115723,
          4.0914225578308105, 4.184331893920898, 4.0529255867004395, 3.7837533950805664,
          3.810925006866455, 3.725015640258789, 3.733659267425537, 3.9179399013519287,
          3.597399950027466, 3.658142328262329, 3.7283573150634766, 3.532588481903076,
          3.5793652534484863, 3.515700578689575, 3.520371913909912, 3.4331295490264893]

forty = [4.804522514343262, 4.3366899490356445, 4.115489482879639, 4.0784382820129395,
         3.907108783721924, 3.7686376571655273, 3.8208045959472656, 3.725247383117676,
         3.647458076477051, 3.6243834495544434, 3.5795624256134033, 3.572613000869751,
         3.572852849960327, 3.5878641605377197, 3.497436046600342, 3.46412992477417,
         3.4096670150756836, 3.4146580696105957, 3.3568356037139893, 3.4282619953155518]

fifty = [4.501245021820068, 4.140755653381348, 4.078004360198975, 4.065719127655029,
         3.8817667961120605, 3.7661116123199463, 3.720968723297119, 3.5888967514038086,
         3.790684461593628, 3.5358409881591797, 3.5749449729919434, 3.482778310775757,
         3.8373963832855225, 3.458265542984009, 3.4774293899536133, 3.4458982944488525,
         3.4003803730010986, 3.3673291206359863, 3.371426820755005, 3.301372766494751]

fifty_two = [4.448215007781982, 4.381494998931885, 4.219041347503662, 4.293772220611572,
             3.8843486309051514, 3.869311809539795, 3.7330164909362793, 3.8038177490234375,
             3.7105376720428467, 3.9600296020507812, 3.6000332832336426, 3.506301164627075,
             3.4831008911132812, 3.453101873397827, 3.404381513595581]


def print_stats():
    print((ten[-1]-fifty[-1])/fifty[-1])
    print((twenty[-1]-fifty[-1])/fifty[-1])
    print((thirty[-1]-fifty[-1])/fifty[-1])
    print((forty[-1]-fifty[-1])/fifty[-1])

    print(sum([max((ten[i]-fifty[i])/fifty[i], 0) for i in range(15,20)])/5)
    print(sum([max((twenty[i]-fifty[i])/fifty[i], 0) for i in range(15,20)])/5)
    print(sum([max((thirty[i]-fifty[i])/fifty[i], 0) for i in range(15,20)])/5)
    print(sum([max((forty[i]-fifty[i])/fifty[i], 0) for i in range(15,20)])/5)


def print_iter_stats():
    sixty = [ten[5],twenty[2],thirty[1], (forty[0]+forty[1])/2, fifty[0]]
    two_hundred = [ten[-1],twenty[9],thirty[6], forty[4], fifty[3]]
    print(two_hundred)
    print((max(two_hundred) - min(two_hundred))/min(two_hundred))



def plot_vs_epoch():
    plt.figure(figsize=(11,5))
    x = range(1,21)
    plt.plot(x, ten, 'o--',label='size 10000')
    plt.plot(x, twenty, 'o--',label='size 20000')
    plt.plot(x, thirty, 'o--',label='size 30000')
    plt.plot(x, forty, 'o--',label='size 40000')
    plt.plot(x, fifty, 'o--',label='size 50000')
    plt.legend(fontsize=14)
    plt.xlabel('number of epochs', fontsize=14)
    plt.ylabel('bits per dimension', fontsize=14)
    plt.title('Validation Set Performance by Epoch for Varying Training Set Sizes', fontsize=20)
    plt.tight_layout()
    plt.show()

def plot_vs_iter():
    plt.figure(figsize=(8,6))
    plt.plot([10000*i for i in range(1,21)], ten, 'o--',label='size 10000')
    plt.plot([20000*i for i in range(1,21)], twenty, 'o--',label='size 20000')
    plt.plot([30000*i for i in range(1,21)], thirty, 'o--',label='size 30000')
    plt.plot([40000*i for i in range(1,21)], forty, 'o--',label='size 40000')
    plt.plot([50000*i for i in range(1,21)], fifty, 'o--',label='size 50000')
    plt.legend()
    plt.xlabel('number of iterations', fontsize=14)
    plt.ylabel('bits per dimension', fontsize=14)
    plt.title('Validation Set Performance by Iteration for Varying Training Set Sizes', fontsize=20)
    plt.tight_layout()
    plt.show()

def map_vs_iter():
    grid = np.ones((5,100))
    maxv = max([max(i) for i in [ten,twenty,thirty,forty,fifty]])
    minv = min([min(i) for i in [ten,twenty,thirty,forty,fifty]])
    grid = grid*maxv

    #grid[0,:20] = ten
    grid[0,:32] = ten_two

    grid[1,1:40:2] = twenty
    grid[1,2:40:2] = [(twenty[i]+twenty[i+1])/2 for i in range(19)]
    grid[1,:1] = twenty[0]

    grid[2,2:60:3] = thirty
    grid[2, 3:60:3] = [2*thirty[i]/3+thirty[i+1]/3 for i in range(19)]
    grid[2, 4:60:3] = [thirty[i]/3+2*thirty[i+1]/3 for i in range(19)]
    grid[2,:2] = thirty[0]

    grid[3,3:80:4] = forty
    grid[3,4:80:4] = [3*forty[i]/4+forty[i+1]/4 for i in range(19)]
    grid[3,5:80:4] = [(forty[i]+forty[i+1])/2 for i in range(19)]
    grid[3,6:80:4] = [forty[i]/4+3*forty[i+1]/4 for i in range(19)]
    grid[3,:3] = forty[0]

    grid[4,4::5] = fifty
    grid[4,5::5] = [4*fifty[i]/5+fifty[i+1]/5 for i in range(19)]
    grid[4,6::5] = [3*fifty[i]/5+2*fifty[i+1]/5 for i in range(19)]
    grid[4,7::5] = [2*fifty[i]/5+3*fifty[i+1]/5 for i in range(19)]
    grid[4,8::5] = [fifty[i]/5+4*fifty[i+1]/5 for i in range(19)]
    grid[4,:4] = fifty[0]

    a = []
    for i in range(40,60):
        a += [(max(grid[2:,i]) - min(grid[2:,i]))/min(grid[2:,i])]
        print(a[-1])
    print(sum(a)/len(a))

    cmap = plt.cm.get_cmap('viridis')
    norm = plt.Normalize(grid.min(),grid.max())
    rgba = cmap(norm(grid))
    rgba[0,32:] = 1,1,1,1
    rgba[1,40:] = 1,1,1,1
    rgba[2,60:] = 1,1,1,1
    rgba[3,80:] = 1,1,1,1

    fig, ax = plt.subplots(figsize=(16,4))
    im = ax.imshow(rgba, aspect=4, vmin=minv, vmax=maxv)

    ax.set_xticks(range(4,100,5))
    ax.set_xticklabels(range(5,101,5))

    ax.set_yticks(range(5))
    ax.set_yticklabels(range(10,55,10))

    plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode="anchor")

    cbar = fig.colorbar(im)
    cbar.set_label('bits per dimension',size=14)

    plt.xlabel("number of iterations (thousands)", fontsize=14)
    plt.ylabel("training set size (thousands)", fontsize=14)
    plt.title("Validation Set Performance in bpd by Iteration for Varying Training Set Sizes", fontsize=20)

    plt.tight_layout()
    plt.show()

#plot_vs_epoch()
#plot_vs_iter()
map_vs_iter()
#print_stats()
#print_iter_stats()

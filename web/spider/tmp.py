import json

beijing_list = ['北京市东城区', '北京市西城区', '北京市朝阳区', '北京市崇文区', '北京市海淀区', '北京市宣武区',
                '北京市石景山区', '北京市门头沟区', '北京市丰台区', '北京市房山区',
                '北京市大兴区', '北京市通州区', '北京市顺义区', '北京市平谷区',
                '北京市昌平区', '北京市怀柔区和延庆县', '北京市密云县']

shanghai = "松江区,青浦区,奉贤区,黄浦区,徐汇区,长宁区,静安区,普陀区,虹口区,杨浦区,闵行区,宝山区,嘉定区,浦东新区,金山区"
shanghai_list = ["上海市"+i for i in shanghai.split(",")]

guangzhou = "荔湾区,越秀区,海珠区,天河区,白云区,黄埔区,番禺区,花都区,南沙区,从化区,增城区"
guangzhou_list = ["广州市"+i for i in guangzhou.split(",")]

shenzhen = "罗湖区,福田区,南山区,宝安区,龙岗区,盐田区"
shenzhen_list = ["深圳市"+i for i in shenzhen.split(",")]

hangzhou = "临安区,上城区,下城区,江干区,拱墅区,西湖区,滨江区,萧山区,余杭区,富阳区"
hangzhou_list = ["杭州市"+i for i in hangzhou.split(",")]

ningbo = "海曙区,江东区,江北区,北仑区,镇海区,鄞州区"
ningbo_list = ["宁波市"+i for i in ningbo.split(",")]

# print(shanghai_list + guangzhou_list + shenzhen_list + hangzhou_list + ningbo_list)



with open("/Users/caosai/Desktop/lbs_all.txt") as fs:
    f = fs.readlines()
    for i in f:
        print(i.strip())
        ii = json.loads(i.replace("'", '"').strip())

        print(type(ii))

        print(ii.get("name"))
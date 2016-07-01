#  -*- coding: utf-8 -*-
__author__ = 'open'




#Naver Open API를 이용하여 네이버 뉴스를 검색하는 크롤러 만들기
#sentece first


import urllib.request
from urllib.request import urlopen
import xml.etree.ElementTree as etree
from pandas import Series, DataFrame
import urllib.parse

from bs4 import BeautifulSoup

default_url='http://openapi.onbid.co.kr/openapi/services/KamcoPblsalThingInquireSvc/getKamcoSaleList'
key='?ServiceKey=e%2FQJDoVfPvWc9YX3chUZREM8xv6vEWgj7EA1yFPeXXKgV17RVWz4VWXXqgNjofV8qash57tMQb8EBIxisAH%2BCg%3D%3D'
sell_type='&SELL_TYPE=ALL'
categ_sys_cd='&CATEG_SYS_CD=000000100001'
categ_sys_cd2='&CATEG_SYS_CD2=000000110001'
goods_address1='&GOODS_ADDRESS1=경북'
open_date='&OPEN_DATE=20160401'
close_date='&CLOSE_DATE=20160431'
numOfRows='&numOfRows=999'
pageSize='&pageSize=999'
pageNo='&pageNo=1'
startPage='&startPage=1'

url=default_url+key+sell_type+categ_sys_cd+categ_sys_cd2+urllib.request.quote(goods_address1)+open_date+close_date+numOfRows+pageSize+pageNo+startPage

file=open("D:\\a.txt","w",encoding='utf-8')

resultXML=urlopen(url.encode("UTF-8").decode("ASCII")).read()
xmlsoup=BeautifulSoup(resultXML,'html.parser')


#resultXML=urlopen(url.encode("ASCII")).read()
#xmlsoup=BeautifulSoup(resultXML,'html.parser')

rnum={}
announce_no={}
auction_no={}
goods_id={}
categ_nm={}
auction_off_no={}
goods_name={}
goods_sku={}
goods_address={}
goods_new_address={}
sell_type={}
auction_method={}
open_price={}
goods_price={}
open_price_rate_view={}
open_date={}
close_date={}
goods_state={}
uscbd_cnt={}
view_cnt={}
manf={}
mdl={}
nrgt={}
grbx={}
endpc={}
vhcl_mlge={}
fuel={}
crpn_nm={}

te=xmlsoup.findAll("item")

i=0

for t in te:
    rnum[i] = t.rnum.string
    announce_no[i] = t.announce_no.string
    auction_no[i] = t.auction_no.string
    goods_id[i] = t.goods_id.string
    categ_nm[i] = t.categ_nm.string
    auction_off_no[i] = t.auction_off_no.string
    goods_name[i] = t.goods_name.string
    goods_sku[i] = t.goods_sku.string
    goods_address[i] = t.goods_address.string
    goods_new_address[i] = t.goods_new_address.string
    sell_type[i] = t.sell_type.string
    auction_method[i] = t.auction_method.string
    open_price[i] = t.open_price.string
    goods_price[i] = t.goods_price.string
    open_price_rate_view[i] = t.open_price_rate_view.string
    open_date[i] = t.open_date.string
    close_date[i] = t.close_date.string
    goods_state[i] = t.goods_state.string
    uscbd_cnt[i] = t.uscbd_cnt.string
    view_cnt[i] = t.view_cnt.string
    manf[i] = t.manf.string
    mdl[i] = t.mdl.string
    nrgt[i] = t.nrgt.string
    grbx[i] = t.grbx.string
    endpc[i] = t.endpc.string
    vhcl_mlge[i] = t.vhcl_mlge.string
    fuel[i] = t.fuel.string
    crpn_nm[i] = t.crpn_nm.string
    i=i+1

#rnum is 'dict type'    print(type(dict))

#rnum_1=frozenset(rnum.items())
#announce_no_1=frozenset(announce_no.items())
#data={announce_no_1,index=rnum_1}
#print(data)
#frame=DataFrame(rnum_1,announce_no_1)
data={'rnum':rnum,'announce_no':announce_no,'auction_no':auction_no,
'goods_id':goods_id,'categ_nm':categ_nm,'auction_off_no':auction_off_no,'goods_name':goods_name,
'goods_sku':goods_sku,'goods_address':goods_address,'goods_new_address':goods_new_address,'sell_type':sell_type,
'auction_method':auction_method,'open_price':open_price,'goods_price':goods_price,'open_price_rate_view':open_price_rate_view,
'open_date':open_date,'close_date':close_date,'goods_state':goods_state,'uscbd_cnt':uscbd_cnt,
'view_cnt':view_cnt,'manf':manf,'mdl':mdl,'nrgt':nrgt,'grbx':grbx,'endpc':endpc,'vhcl_mlge':vhcl_mlge,
'fuel':fuel,'crpn_nm':crpn_nm}

frame=DataFrame(data,columns=["rnum","announce_no",'auction_no',
'goods_id','categ_nm','auction_off_no','goods_name','goods_sku','goods_address',
'goods_new_address','sell_type','auction_method','open_price','goods_price','open_price_rate_view',
'open_date','close_date','goods_state','uscbd_cnt','view_cnt','manf','mdl','nrgt','grbx','endpc',
'vhcl_mlge','fuel','crpn_nm'])

#print(frame)


#data.to_csv(sys.stdout, sep='|')

#group sum
frame['gn_class']=frame.goods_name.str[0:2]
#print(frame.gn_class)

print(frame.groupby("gn_class").count())




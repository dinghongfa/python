from selenium import webdriver
from time import sleep
import pandas as pd
import os
from sys import argv
import time
from datetime import datetime
from progressbar import ProgressBar


def drop_zero_row(df):
	cols = list(df.cookie_id_cur)
	while '0_0' in cols:
		cols.remove('0_0')
	return df[df.cookie_id_cur.isin(cols)]


if __name__ == '__main__':
	print('''
	
 ___    _____  ___                        _                                              _   
|  _`\ (  _  )(  _`\                     ( )_                                  _        ( )_ 
| (_) )| (_) || (_(_)         _ _  _   _ | ,_)   _           ___    ___  _ __ (_) _ _   | ,_)
| ,  / |  _  |`\__ \        /'_` )( ) ( )| |   /'_`\       /',__) /'___)( '__)| |( '_`\ | |  
| |\ \ | | | |( )_) |      ( (_| || (_) || |_ ( (_) )      \__, \( (___ | |   | || (_) )| |_ 
(_) (_)(_) (_)`\____)      `\__,_)`\___/'`\__)`\___/'      (____/`\____)(_)   (_)| ,__/'`\__)
                     ______                          ______                      | |         
                    
																										__version:2.0
																										__author:wai&parson
''')
	today = datetime.now().strftime('%Y-%m-%d')
	today_time = datetime.now().strftime('%Y-%m-%d-%H:%M')
	print('<-----------------------------------'
						'{time}'
		  '------------------------------------>'.format(time=today_time))
	#LOGIN RSA!
	print('初始化浏览器...')
	try:
		#option = webdriver.ChromeOptions()
		#option.add_argument('headless')
		browser = webdriver.Chrome()
	except:
		print('初始化浏览器失败，检查是否安装正确版本Chrome浏览器，驱动，和Selenium')
		
	print('初始浏览器成功!')
	
	
	print('登录中...')
	try:
		browser.get(url='https://139.199.250.168:20145/overview/?y7bRbP=rAxrqGr6w6w6w6w6wazQKgZh7ycMRWiC6Un.Jt_xR9Y6')
	except:
		print('网络连接失败，请检查网络')
	try:
		browser.find_element_by_class_name('group').find_element_by_name('username').send_keys('admin')
		browser.find_element_by_class_name('group').find_element_by_name('password').send_keys('gzcb@ras18!')
	except:
		print('账号密码错误')
		
	browser.find_element_by_xpath('//button[@*]').click()
	sleep(2)
	print('登录成功!')
	
	

	
	#打开Cookie搜索页面
	print('打开Cookie页面...')
	cookie_1='window.open("https://139.199.250.168:20145/phoenix/zh-CN/app/phoenix/search?s=%2FservicesNS%2Fphoenix_admin%2Fphoenix%2Fsaved%2Fsearches%2F%25E7%25BB%259F%25E8%25AE%25A1-%25E4%25BB%25A3%25E5%258A%259E%25E8%25BF%259B%25E4%25BB%25B6%2528Cookie%2529&sid=1531187861.250714&display.page.search.mode=smart&dispatch.sample_ratio=1&q=search%20index%3D%22access_log%22%20business_cookie%3D%22*phone*%22%20%7C%20rex%20field%3Dbusiness_cookie%20%22phone%3D(%3F%3CPhone_Num%3E%5Cd%7B11%7D)%22%20%7C%20rex%20field%3Dbusiness_cookie%20%22userName%3D(%3F%3CUser_Name%3E%5CS%7B3%2C4%7D)%22%20%7C%20rex%20field%3Dbusiness_cookie%20%22city%3D(%3F%3Ccity%3E%5CS%7B3%7D)%22%20%7C%20rex%20field%3Dbusiness_cookie%20%22area%3D(%3F%3Carea%3E%5CS%7B3%7D)%22%20%7C%20eval%20Access_Time%3Dstrftime(_time%2C%22%25Y-%25m-%25d%20%22)%20%7C%20stats%20values(Access_Time)%2Cdc(User_Name)%20as%20dcUserName%20%2C%20values(User_Name)%20dc(Phone_Num)%20%2C%20values(Phone_Num)%20dc(city)%20values(city)%20dc(area)%20values(area)%20by%20cookie_id_cur%20%7C%20search%20dcUserName%20%3E%201&earliest=0&latest=");'
	browser.execute_script(cookie_1)
	sleep(1)
	#打开Cookie搜索页面（自己添加表达式）
	cookie_2='window.open("https://139.199.250.168:20145/phoenix/zh-CN/app/phoenix/search?s=%2FservicesNS%2Fphoenix_admin%2Fphoenix%2Fsaved%2Fsearches%2F%25E7%25BB%259F%25E8%25AE%25A1-%25E4%25BB%25A3%25E5%258A%259E%25E8%25BF%259B%25E4%25BB%25B6%2528Cookie%2529&display.page.search.mode=smart&dispatch.sample_ratio=1&q=search%20index%3D%22access_log%22%20business_cookie%3D%22*phone*%22%20%7C%20rex%20field%3Dbusiness_cookie%20%22phone%3D(%3F%3CPhone_Num%3E%5Cd%7B11%7D)%22%20%7C%20rex%20field%3Dbusiness_cookie%20%22userName%3D(%3F%3CUser_Name%3E%5CS%7B3%2C4%7D)%22%20%7C%20rex%20field%3Dbusiness_cookie%20%22city%3D(%3F%3Ccity%3E%5CS%7B3%7D)%22%20%7C%20rex%20field%3Dbusiness_cookie%20%22area%3D(%3F%3Carea%3E%5CS%7B3%7D)%22%20%7C%20search%20Phone_Num%3D*%20%7C%20eval%20Access_Time%3Dstrftime(_time%2C%22%25Y-%25m-%25d%20%22)%20%7C%20table%20cookie_id_cur%2CAccess_Time%2CPhone_Num%2CUser_Name%2Ccity%2Carea&earliest=0&latest=&sid=1531189715.250871");'
	browser.execute_script(cookie_2)
	sleep(1)
	#打开Post_data搜索页面
	print('打开Post_data搜索页面...')
	post_date_1='window.open("https://139.199.250.168:20145/phoenix/zh-CN/app/phoenix/search?s=%2FservicesNS%2Fphoenix_admin%2Fphoenix%2Fsaved%2Fsearches%2F%25E7%25BB%259F%25E8%25AE%25A1-%25E4%25BB%25A3%25E5%258A%259E%25E6%2589%25B9%25E9%2587%258F%25E8%25BF%259B%25E4%25BB%25B6%2528post%2520data%2529&display.page.search.mode=fast&dispatch.sample_ratio=1&q=search%20index%3D%22access_log%22%20%7Crex%20field%3Dbusiness_post_data%20%22ID_NUM%3D(%3F%3CID_Num%3E%5B0-9a-zA-Z%5D%7B32%7D)%22%20%7Crex%20field%3Dbusiness_post_data%20%22ID_CARD%3D(%3F%3CID_Card_Num%3E%5Cd%7B17%7D(%5Cd%7CX%7Cx))%22%20%7C%20rex%20field%3Dbusiness_post_data%20%22USER_NAME%3D(%3F%3CUser_Name%3E%5CS*%3F)(%26)%22%20%7C%20rex%20field%3Dbusiness_post_data%20%22MOBILE%3D(%3F%3CPhone_Num%3E%5Cd%7B11%7D)%22%20%7C%20rex%20field%3Dbusiness_post_data%20%22COMPANYADDR1%3D(%3F%3CCOMPANYADDR%3E%5CS*%3F)(%26)%22%20%7Crex%20field%3Dbusiness_post_data%20%22COMPANY%3D(%3F%3CCOMPANY%3E%5CS*%3F)(%26)%22%20%7C%20eval%20Access_Time%3Dstrftime(_time%2C%22%25Y-%25m-%25d%20%22)%20%7C%20stats%20values(Access_Time)%2Cdc(User_Name)%20as%20dcUser_Name%2C%20values(User_Name)%2C%20dc(Phone_Num)%20as%20dcPhone_Num%2C%20values(Phone_Num)%2Cdc(COMPANYADDR)%20values(COMPANYADDR)%2C%20dc(COMPANY)%20values(COMPANY)%20by%20cookie_id_cur%20%7C%20search%20(dcID_Card_Num%20%3E%201%20OR%20dcPhone_Num%20%3E1)%20dcUser_Name%20%3E%201&earliest=0&latest=&sid=1531187579.250571");'
	browser.execute_script(post_date_1)
	sleep(1)
	#打开Post_data搜索页面（自己添加表达式）
	post_date_2='window.open("https://139.199.250.168:20145/phoenix/zh-CN/app/phoenix/search?s=%2FservicesNS%2Fphoenix_admin%2Fphoenix%2Fsaved%2Fsearches%2F%25E7%25BB%259F%25E8%25AE%25A1-%25E4%25BB%25A3%25E5%258A%259E%25E6%2589%25B9%25E9%2587%258F%25E8%25BF%259B%25E4%25BB%25B6%2528post%2520data%2529&display.page.search.mode=fast&dispatch.sample_ratio=1&q=search%20index%3D%22access_log%22%20NOT%20cookie_id_cur%3D0_0%20%20%7Crex%20field%3Dbusiness_post_data%20%22ID_NUM%3D(%3F%3CID_Num%3E%5B0-9a-zA-Z%5D%7B32%7D)%22%20%7Crex%20field%3Dbusiness_post_data%20%22ID_CARD%3D(%3F%3CID_Card_Num%3E%5Cd%7B17%7D(%5Cd%7CX%7Cx))%22%20%7C%20rex%20field%3Dbusiness_post_data%20%22USER_NAME%3D(%3F%3CUser_Name%3E%5CS*%3F)(%26)%22%20%7C%20rex%20field%3Dbusiness_post_data%20%22MOBILE%3D(%3F%3CPhone_Num%3E%5Cd%7B11%7D)%22%20%7C%20rex%20field%3Dbusiness_post_data%20%22COMPANYADDR1%3D(%3F%3CCOMPANYADDR%3E%5CS*%3F)(%26)%22%20%7Crex%20field%3Dbusiness_post_data%20%22COMPANY%3D(%3F%3CCOMPANY%3E%5CS*%3F)(%26)%22%7C%20search%20Phone_Num%3D*%20%7C%20eval%20Access_Time%3Dstrftime(_time%2C%22%25Y-%25m-%25d%20%22)%20%7C%20table%20cookie_id_cur%2CAccess_Time%2CPhone_Num%2CUser_Name%2CCOMPANY%2CCOMPANYADDR&earliest=0&latest=&sid=1531189190.250832");'
	browser.execute_script(post_date_2)
	sleep(1)
	
	
	
	sleep(5)
	all_handles = browser.window_handles#获取全部页面句柄
	#print(all_handles)
	
	
	#进行搜索
	sleep(1)
	browser.switch_to.window(all_handles[1])
	browser.find_element_by_class_name('search-button').find_element_by_class_name('btn').click()
	sleep(1)
	
	browser.switch_to.window(all_handles[2])
	browser.find_element_by_class_name('search-button').find_element_by_class_name('btn').click()
	sleep(1)

	browser.switch_to.window(all_handles[3])
	browser.find_element_by_class_name('search-button').find_element_by_class_name('btn').click()
	sleep(1)

	browser.switch_to.window(all_handles[4])
	browser.find_element_by_class_name('search-button').find_element_by_class_name('btn').click()
	sleep(1)
	#ProgressBar
	pbar = ProgressBar(maxval = 2400)
	print('正在进行搜索...')
	for i in range(0,40*60):
		pbar.start()
		pbar.update(i)
		sleep(1)

	pbar.finish()
	print('搜索完成！')
	
	
	#进行下载日志
	print('正在下载文件...')
	browser.switch_to.window(all_handles[1])
	browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div[1]/div[2]/div[2]/a[3]').click()
	sleep(2)
	browser.find_element_by_name('fileName').send_keys(today+'-post_date_2')
	browser.find_element_by_link_text('导出').click()
	sleep(5)
	browser.switch_to.window(all_handles[2])
	browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div[1]/div[2]/div[2]/a[3]').click()
	sleep(2)
	browser.find_element_by_name('fileName').send_keys(today+'-post_date_1')
	browser.find_element_by_link_text('导出').click()
	
	browser.switch_to.window(all_handles[3])
	browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div[1]/div[2]/div[2]/a[3]').click()
	sleep(2)
	browser.find_element_by_name('fileName').send_keys(today+'-cookie_2')
	browser.find_element_by_link_text('导出').click()
	
	browser.switch_to.window(all_handles[4]
	browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div[1]/div[2]/div[2]/a[3]').click()
	sleep(2)
	browser.find_element_by_name('fileName').send_keys(today+'-cookie_1')
	browser.find_element_by_link_text('导出').click()
	sleep(60)
	print('下载完成!')
	

	#browser.quit()

	#开始整合
	os.chdir('C:\\Users\\m1867\\Downloads')
	#print(os.getcwd())
	print('开始整合...')
	fname = '代办进件'
	if len(argv) == 2:
		fname += argv[1] + '.xlsx'
	else:
		fname += time.strftime("%m%d") + '.xlsx'
	f1 = open(today+'-cookie_1.csv', encoding='utf-8')
	df_cookie = pd.DataFrame(pd.read_csv(f1))
	f2 = open(today+'-post_date_1.csv', encoding='utf-8')
	df_postdata = pd.DataFrame(pd.read_csv(f2))
	df_postdata = df_postdata.drop(['dcID_Card_Num'], axis=1)
	df_postdata.columns = df_cookie.columns
	df_merged = pd.concat([df_cookie, df_postdata])
	df_merged = drop_zero_row(df_merged)
	df_merged = df_merged.sort_values(by='dcUserName', ascending=False)
	f3 = open(today+'-cookie_2.csv', encoding='utf-8')
	df_cookie_detail   = pd.DataFrame(pd.read_csv(f3))
	try:
		f4 = open(today+'-post_date_2.csv', encoding='utf-8')
	except:
		print('整合失败了TAT 嘤嘤嘤，确认今天的post_date_2.csv 下载完成 然后在( 下载 )目录下重新运行script.py')
	df_postdata_detail = pd.DataFrame(pd.read_csv(f4))
	df_postdata_detail.columns = df_cookie_detail.columns
	df_detail_merged = pd.concat([df_cookie_detail, df_postdata_detail])
	df_detail_merged = drop_zero_row(df_detail_merged)
	df_detail_merged = df_detail_merged.drop_duplicates(['cookie_id_cur', 'Phone_Num', 'User_Name'])
	Search_Array = list(df_merged.cookie_id_cur)
	users = list(df_detail_merged.cookie_id_cur)
	suspect = [u for u in users if u in Search_Array]
	df_detail_merged = df_detail_merged[df_detail_merged.cookie_id_cur.isin(suspect)]
	df_detail_merged = df_detail_merged.sort_values(by='Access_Time', ascending=False)
	writer = pd.ExcelWriter(fname)
	df_merged.to_excel(writer, index=False, sheet_name='疑似代办')
	df_detail_merged.to_excel(writer, index=False, sheet_name='详细信息')
	writer.save()
	print("Finish")
	#复制文件
	os.system("copy {} {}".format(fname,'C:\\Users\\m1867\\Desktop\\parsons\\代办进件\\' + fname))

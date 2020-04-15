# coding=utf-8
from selenium import webdriver
import time
import pandas as pd
import os
import shutil
########################################
"""
爬取中国移动采购和供应商公告
网址: https://b2b.10086.cn/b2b/main/listVendorNotice.html?noticeType=2#this
"""

# 打开网页
def open_window(url):
    # 指定无界面形式运行
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=chromeOptions)
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

# 爬取公告当前页的基本信息
def get_text(driver, flag):
    if flag == 0:
        # 一采供应商
        df_ancm = pd.DataFrame(columns=["公告类型", "标题", "时间", "链接"])
    elif flag == 1:
        # 二采供应商
        df_ancm = pd.DataFrame(columns=["公告类型", "公告发布单位", "标题", "时间", "链接"])
    else:
        # 招标采购
        df_ancm = pd.DataFrame(columns=["采购需求单位", "公告类型", "标题", "时间", "链接"])

    # 爬取当前页的所有[单位 类型 标题 时间]
    allAncm = driver.find_elements_by_xpath('//*[@id="searchResult"]/table/tbody/tr')

    # 公告内容所有id
    pageTitleId = []

    for i in range(2, allAncm.__len__()):
        ancm = allAncm[i].text
        print('  |-' + i.__str__() + ancm)
        # 获取公告详细标题
        title = allAncm[i].find_element_by_tag_name('a').get_attribute('title')

        # 缓存所有标题id
        idStr = allAncm[i].get_attribute('onclick')
        id = idStr[idStr.find('\'')+1:idStr.rfind('\'')]
        pageTitleId.append(id)

        # 分割标题分别获取[单位 类型 标题 时间]
        # 时间
        indexTime = ancm.rindex(' ')
        ancmTime = ancm[indexTime+1:]

        if flag == 0:
            # 一采供应商
            # 标题
            index0 = ancm.index(' ')
            ancmTitle = ancm[index0+1:indexTime]
            # 链接
            ancmLink = 'https://b2b.10086.cn/b2b/main/viewVendorNoticeContent.html?noticeBean.id=' + id

            # 保存到df
            ancmList = [{"公告类型": '一采供应商公告', "标题": title if title else ancmTitle, "时间": ancmTime, "链接": ancmLink}]
            df_ancm = df_ancm.append(pd.DataFrame(ancmList, columns=["公告类型", "标题", "时间", "链接"]),
                                     ignore_index=True)
        elif flag == 1:
            # 二采供应商
            # 公告发布单位
            index0 = ancm.index(' ')
            index1 = ancm.index(' ', index0+1)
            ancmUnit = ancm[index0:index1]
            # 标题
            ancmTitle = ancm[index1+1:indexTime]
            # 链接
            ancmLink = 'https://b2b.10086.cn/b2b/main/viewVendorNoticeContent.html?noticeBean.id=' + id

            # 保存到df
            ancmList = [{"公告类型": '二采供应商公告', "公告发布单位": ancmUnit,
                         "标题": title if title else ancmTitle, "时间": ancmTime, "链接": ancmLink}]
            df_ancm = df_ancm.append(pd.DataFrame(ancmList, columns=["公告类型", "公告发布单位", "标题", "时间", "链接"]),
                                     ignore_index=True)
        else:
            # 招标采购
            # 单位
            index0 = ancm.index(' ')
            ancmUnit = ancm[:index0]
            # 类型
            index1 = ancm.index(' ', index0+1)
            ancmType = ancm[index0+1:index1]
            # 标题
            ancmTitle = ancm[index1+1:indexTime]
            # 链接
            ancmLink = 'https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeBean.id=' + id

            # 保存到df
            ancmList = [{"采购需求单位": ancmUnit, "公告类型": ancmType,
                         "标题": title if title else ancmTitle, "时间": ancmTime, "链接": ancmLink}]
            df_ancm = df_ancm.append(pd.DataFrame(ancmList, columns=["采购需求单位", "公告类型", "标题", "时间", "链接"]),
                                     ignore_index=True)
    return pageTitleId, df_ancm

# 爬取所有公告的具体内容
def get_content(contentUrl, allTitleId):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    contentList = []
    i = 1
    for id in allTitleId:
        driver.get(contentUrl + str(id))
        print('公告内容' + i.__str__() + ' : ' + id + ' : ' + driver.find_element_by_xpath(
            '//*[@id="container"]/div[1]/table/tbody/tr[2]').text)
        # time.sleep(0.5)
        i += 1
        content = driver.find_element_by_xpath('//*[@id="container"]/div[1]/table/tbody')
        # 缓存公告内容
        contentList.append(content.text)
    driver.close()
    return contentList

# 搜索两个日期间的所有公告
def dateSearch(driver, startDate, endDate):
    print('公告日期: ' + startDate + ' - ' + endDate)
    driver.find_element_by_xpath('//*[@id="startDate"]').send_keys(startDate)
    driver.find_element_by_xpath('//*[@id="endDate"]').send_keys(endDate)
    driver.find_element_by_xpath('//*[@id="search"]').click()
    time.sleep(3)

# 爬取所有招标采购公告
def get_zbcgAncm(driver, filePath, startDate, endDate):
    # 获取所有公告类型
    allAncmType = driver.find_elements_by_xpath('//*[@id="container"]/div[1]/table/tbody/tr/td[1]/ul/li')

    # 搜索两个日期间的所有公告
    print('开始搜索公告...')
    dateSearch(driver, startDate, endDate)
    print('公告搜索完成...')

    # 循环爬取所有类型公告
    for i in range(allAncmType.__len__()):
        # 点击公告类型
        print('开始搜索' + allAncmType[i].text + '...')
        allAncmType[i].click()
        time.sleep(5)

        # 当前类型公告df
        df_thisAncm = pd.DataFrame(columns=["采购需求单位", "公告类型", "标题", "时间", "链接", "公告内容"])

        # 判断是否为空
        tb = driver.find_element_by_xpath('//*[@id="searchResult"]').text
        # 未加载完全
        while tb == '':
            print('请稍等...')
            time.sleep(1)

        if tb == '查无结果！':
            print('数据为空...')
            # 保存到csv
            df_thisAncm.to_csv(filePath + str(i) + allAncmType[i].text + '.csv', encoding='utf-8-sig', index=False)
            continue

        # 判断日期是否正确
        ancmDate = driver.find_element_by_xpath('//*[@id="searchResult"]/table/tbody/tr[3]/td[4]')
        dateTmp = time.strftime('%Y-%m-%d', time.strptime(ancmDate.text, '%Y-%m-%d'))
        while dateTmp != endDate and dateTmp > endDate:
            print('重新获取日期...')
            driver.find_element_by_xpath('//*[@id="search"]').click()
            time.sleep(3)
            ancmDate = driver.find_element_by_xpath('//*[@id="searchResult"]/table/tbody/tr[3]/td[4]')
            dateTmp = time.strftime('%Y-%m-%d', time.strptime(ancmDate.text, '%Y-%m-%d'))

        # 判断公告是否点击成功
        ancmType = driver.find_element_by_xpath('//*[@id="searchResult"]/table/tbody/tr[3]/td[2]')
        while ancmType.text != allAncmType[i].text:
            print('重新获取公告...')
            allAncmType[i].click()
            time.sleep(5)
            ancmType = driver.find_element_by_xpath('//*[@id="searchResult"]/table/tbody/tr[3]/td[2]')

        # 开始爬取数据
        print('开始爬取' + allAncmType[i].text)
        j = 1
        allTitleId = []
        df_content = pd.DataFrame()
        while True:
            # 爬取当前页的公告
            print('开始爬取第' + j.__str__() + '页公告...')
            while True:
                try:
                    pageTitleId, df_ancm = get_text(driver, 2)
                    # 判断是否重复爬取
                    if j > 1 and pageTitleId[-1] == allTitleId[-1]:
                        raise Exception
                    allTitleId = pageTitleId
                    df_thisAncm = df_thisAncm.append(df_ancm, ignore_index=True)
                    break
                except Exception as e:
                    # print(e)
                    print('重新爬取第' + j.__str__() + '页公告...')
                    time.sleep(3)
            j += 1

            print('开始爬取公告具体内容...')
            contentUrl = 'https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeBean.id='
            allContent = get_content(contentUrl, allTitleId)
            print('公告内容爬取完成...')

            print('开始合并基本信息和公告内容...')
            # 公告内容df
            df_content = df_content.append(pd.DataFrame(allContent), ignore_index=True)
            # 合并基本信息和公告内容并保存
            df_thisAncm['公告内容'] = df_content

            # 保存为csv
            df_thisAncm.to_csv(filePath + str(i) + allAncmType[i].text + '.csv', encoding='utf-8-sig', index=False,
                               columns=["采购需求单位", "公告类型", "标题", "时间", "链接", "公告内容"])
            print('合并基本信息和公告内容完成...')

            # 点击下一页
            try:
                driver.find_element_by_xpath('//*[@id="pageid2"]/table/tbody/tr/td[4]/a').click()
                time.sleep(3)
            except:
                print('所有页爬取完成...')
                break
        print('共' + str(allTitleId.__len__()) + '篇公告...')
        print('保存' + allAncmType[i].text + '完成...')
    print('所有公告爬取完成...')

# 爬取所有供应商公告
def get_gysAncm(driver, filePath, startDate, endDate):
    # 获取所有供应商公告
    allGysType = driver.find_elements_by_xpath('//*[@id="container"]/div[1]/table/tbody/tr/td[1]/ul[2]/li')

    # 循环爬取供应商公告
    for i in range(allGysType.__len__()):
        # 点击公告类型
        print('开始搜索' + allGysType[i].text + '...')
        allGysType[i].click()
        time.sleep(5)

        # 搜索两个日期间的所有公告
        print('开始搜索公告...')
        dateSearch(driver, startDate, endDate)
        print('公告搜索完成...')

        # 当前类型公告df
        if i == 0:
            df_thisAncm = pd.DataFrame(columns=["公告类型", "标题", "时间", "链接"])
        else:
            df_thisAncm = pd.DataFrame(columns=["公告类型", "公告发布单位", "标题", "时间", "链接"])

        # 判断是否为空
        tb = driver.find_element_by_xpath('//*[@id="searchResult"]').text
        # 未加载完全
        while tb == '':
            print('请稍等...')
            time.sleep(1)

        if tb == '查无结果！':
            print('数据为空...')
            # 保存到csv
            df_thisAncm.to_csv(filePath + str(6+i) + allGysType[i].text + '.csv',
                               encoding='utf-8-sig', index=False)
            continue

        # 判断日期是否正确
        tmpAncm = driver.find_element_by_xpath('//*[@id="searchResult"]/table/tbody/tr[3]').text
        ancmDate = tmpAncm[tmpAncm.rfind(' ')+1:]
        dateTmp = time.strftime('%Y-%m-%d', time.strptime(ancmDate, '%Y-%m-%d'))
        while dateTmp != endDate and dateTmp > endDate:
            print('重新获取日期...')
            driver.find_element_by_xpath('//*[@id="search"]').click()
            time.sleep(3)
            tmpAncm = driver.find_element_by_xpath('//*[@id="searchResult"]/table/tbody/tr[3]')
            ancmDate = tmpAncm[tmpAncm.rfind(' ')+1:]
            dateTmp = time.strftime('%Y-%m-%d', time.strptime(ancmDate, '%Y-%m-%d'))

        # 开始爬取数据
        print('开始爬取' + allGysType[i].text)
        # 当前类型公告df
        if i == 0:
            df_thisAncm = pd.DataFrame(columns=["公告类型", "标题", "时间", "链接"])
        else:
            df_thisAncm = pd.DataFrame(columns=["公告类型", "公告发布单位", "标题", "时间", "链接"])
        j = 1
        allTitleId = []
        df_content = pd.DataFrame()
        while True:
            # 爬取当前页的公告
            print('开始爬取第' + j.__str__() + '页公告...')
            while True:
                try:
                    pageTitleId, df_ancm = get_text(driver, i)
                    # 判断是否重复爬取
                    if j > 1 and pageTitleId[-1] == allTitleId[-1]:
                        raise Exception
                    allTitleId += pageTitleId
                    df_thisAncm = df_thisAncm.append(df_ancm, ignore_index=True)
                    break
                except Exception as e:
                    # print(e)
                    print('重新爬取第' + j.__str__() + '页公告...')
                    time.sleep(3)
            j += 1

            print('开始爬取公告具体内容...')
            contentUrl = 'https://b2b.10086.cn/b2b/main/viewVendorNoticeContent.html?noticeBean.id='
            allContent = get_content(contentUrl, allTitleId)
            print('公告内容爬取完成...')

            print('开始合并基本信息和公告内容...')
            # 公告内容df
            df_content = df_content.append(pd.DataFrame(allContent), ignore_index=True)
            # 合并基本信息和公告内容并保存
            df_thisAncm['公告内容'] = df_content

            if i == 0:
                dfcolumns = ["公告类型", "标题", "时间", "链接", "公告内容"]
            else:
                dfcolumns = ["公告类型", "公告发布单位", "标题", "时间", "链接", "公告内容"]

            # 保存为csv
            df_thisAncm.to_csv(filePath + str(6+i) + allGysType[i].text + '.csv',
                               encoding='utf-8-sig', index=False, columns=dfcolumns)
            print('合并基本信息和公告内容完成...')

            # 点击下一页
            try:
                driver.find_element_by_xpath('//*[@id="pageid2"]/table/tbody/tr/td[4]/a').click()
                time.sleep(3)
            except:
                print('基本信息爬取完成...')
                break
        print('共' + str(allTitleId.__len__()) + '篇公告...')
        print(allGysType[i].text + '爬取完成...')
    print('所有公告爬取完成...')

# 合并csv
def merge_allAncm(filePath, startDate, endDate):
    allFile = os.listdir(filePath)

    # 设定文件名前缀
    seDate = startDate.replace('-', '')[4:] + '-' + endDate.replace('-', '')[4:]

    writer = pd.ExcelWriter(filePath + seDate +'招标及供应商公告.xlsx')
    print('开始合并csv...')
    for i in range(allFile.__len__()):
        tmpPath = filePath + allFile[i]
        fileSize = os.path.getsize(tmpPath)
        sheetName = allFile[i][1:-4]
        if fileSize:
            tmpDf = pd.read_csv(tmpPath, encoding='utf-8-sig', engine='python')
            tmpDf.to_excel(writer, encoding='utf-8-sig', index=False, sheet_name=sheetName)
    print('合并csv完成...')
    writer.save()

# 转移文件
def move_file(filePath, startDate, endDate, moveFilePath):
    # 创建目录
    seDate = startDate.replace('-', '')[4:] + '-' + endDate.replace('-', '')[4:]
    dir = moveFilePath + seDate
    if not os.path.exists(dir):
        os.mkdir(dir)
        print('创建目录成功: ' + dir)
    else:
        print('目录已存在...')

    # 转移文件
    allFile = os.listdir(filePath)
    if not allFile:
        print('没有文件可转移...')
        return

    for i in range(len(allFile)):
        shutil.move(filePath + allFile[i], dir)
        print(allFile[i] + '移动完成...')

def main(filePath, startDate, endDate):
    print('----- 开始爬虫任务 -----')
    driver = open_window('https://b2b.10086.cn/b2b/main/listVendorNotice.html?noticeType=2#this')

    # 爬取所有招标采购公告
    print('开始爬取招标采购公告...')
    get_zbcgAncm(driver, filePath, startDate, endDate)
    print('爬取招标采购公告完成...')

    # 爬取所有供应商公告
    driver.get('https://b2b.10086.cn/b2b/main/preSupplierManagement.html#this')
    print('开始爬取供应商公告...')
    get_gysAncm(driver, filePath, startDate, endDate)
    print('爬取供应商公告完成...')

    # 合并csv
    print('开始合并公告到xlsx...')
    merge_allAncm(filePath, startDate, endDate)
    print('合并公告到xlsx完成...')

    # 转移文件
    print('开始转移文件...')
    moveFilePath = r'C:\PythonProject\移动公告采集\\'
    move_file(filePath, startDate, endDate, moveFilePath)
    print('转移文件完成...')

    print('----- 爬虫任务结束 -----')

if __name__ == '__main__':
    startDate = '2019-04-16'
    endDate = '2019-04-22'
    filePath = r'C:\PythonProject\ChinaMobile\\'
    main(filePath, startDate, endDate)
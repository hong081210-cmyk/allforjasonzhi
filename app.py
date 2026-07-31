import streamlit as st
import json
import os

# 设置网页标题和图标
st.set_page_config(page_title="销售额实时对比大盘", page_icon="📊", layout="centered")

# 强制网页自动刷新（这里设置为每 5 秒刷新一次网页，捕捉最新的数据变动）
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=5000, key="datarefresh")

st.title("📊 销售额实时对比大盘")
st.write("---")

# 读取数据文件
if os.path.exists("live_data.json"):
    try:
        with open("live_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # 1. 渲染冠亚军看板
        st.subheader(f"🥇 {data['first_name']}: {data['first_sales']}")
        st.subheader(f"🥈 {data['second_name']}: {data['second_sales']}")
        
        st.write("---")
        
        # 2. 渲染实时战况提示框
        if "领先" in data['status']:
            st.info(data['status'])
        else:
            st.success(data['status'])
            
        # 3. 显示最后更新时间
        st.caption(f"数据最后更新时间: {data['update_time']} (网页每5秒自动刷新)")
        
    except Exception as e:
        st.warning("正在等待爬虫写入首批完整数据...")
else:
    st.warning("⏳ 暂无大盘数据，请等待本地后台爬虫 `crawler.py` 同步数据。")

"""Regenerate the public PDF: pip install reportlab, then python tools/build_resume.py.
Set RESUME_FONT and RESUME_FONT_BOLD for Chinese TrueType fonts on other systems.
"""
from pathlib import Path
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

ROOT = Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(TTFont('Chinese', os.environ.get('RESUME_FONT', 'C:/Windows/Fonts/msyh.ttc'), subfontIndex=0))
pdfmetrics.registerFont(TTFont('ChineseBold', os.environ.get('RESUME_FONT_BOLD', 'C:/Windows/Fonts/msyhbd.ttc'), subfontIndex=0))
pdfmetrics.registerFontFamily('Chinese', normal='Chinese', bold='ChineseBold')
navy = colors.HexColor('#102a43')
muted = colors.HexColor('#526577')
body = ParagraphStyle('body', fontName='Chinese', fontSize=9, leading=14.8, textColor=navy, spaceAfter=4)
small = ParagraphStyle('small', parent=body, fontSize=8, leading=12, textColor=muted)
section_style = ParagraphStyle('section', parent=body, fontName='ChineseBold', fontSize=11.2, leading=16, spaceBefore=12, spaceAfter=7)
name_style = ParagraphStyle('name', parent=body, fontName='ChineseBold', fontSize=25, leading=34)
right = ParagraphStyle('right', parent=small, alignment=TA_RIGHT)
story = []
def p(text, style=body):
    return Paragraph(text, style)
def section(title):
    story.append(p(title, section_style))
    story.append(HRFlowable(width='100%', thickness=.5, color=colors.HexColor('#ced8e1'), spaceAfter=7))
def row(left, date):
    t = Table([[p(left), p(date, right)]], colWidths=[360, 151])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    story.append(t)

story.extend([p('罗顿', name_style), p('金融学本科 · 2027届｜求职方向：金融 / 财务 / 银行 / 审计 / 数据分析'), p('邮箱：<link href="mailto:1932370757@qq.com" color="#27608a">1932370757@qq.com</link>', small)])
section('教育经历')
row('<b>湖南工商大学</b>｜金融学 · 本科', '2023.09 - 2027.06')
story.append(p('预计2027年6月毕业。', small))
row('<b>弗罗斯特堡州立大学</b>｜理学本科', '2023.09 - 2027.06')
section('实习经历')
row('<b>湖南建湘工程建设有限公司</b>', '2026.07 - 2026.09')
story.append(p('项目成本与物资管理实习生｜湘钢技改项目部'))
for text in [
    '<b>资金管理：</b>独立编制并维护银行付款台账，覆盖28笔对公付款、累计支出70余万元；按项目用途、收款方及月份汇总，与银行流水逐笔核对，实现月度账款零差异。',
    '<b>账务核对：</b>核对银行回单、付款申请及收款信息，识别2笔因账号或户名不符导致的退回款项，合计5千余元，协助完成追溯、销账及重新支付。',
    '<b>成本核算：</b>参与17项现场签证的工程量计量及资料编制，涉及合同外工程量金额60余万元；按“工程量 × 甲供材除税单价”归集主材成本，完成钢筋150余吨、50余万元成本核算。',
    '<b>物资管理：</b>参与高压电气室钢材计划编制，完成24项材料规格与理论重量核算，累计16余吨；依据4项国标校核参数。',
]: story.append(p(text))
section('科研项目与成果')
row('<b>数字普惠金融助力乡村产业高质量发展研究</b>', '2024.03 - 2026.06')
story.append(p('大学生创新创业大赛项目｜项目小组主干成员'))
story.append(p('<b>分析工作：</b>收集63家乡村产业负责人的数字普惠金融使用及经营数据，完成数据整理、统计分析及回归分析，为研究结论提供实证支持。'))
story.append(p('<b>项目成果：</b>项目获国家级立项；项目证书及公开链接待补充。'))
story.append(p('<b>论文成果：</b>《数字普惠金融助力乡村产业高质量发展的对策研究》。《山西农经》，录用待刊，拟刊2026年第22期。'))
story.append(p('<b>作者署名：</b>王柯理、袁佳豪、<b>罗顿</b>、朱逸骁、陈栋；本人为第三作者（依据稿件录用通知）。论文公开链接待补充。'))
section('专业技能与作品')
for text in [
    '<b>Excel与财务：</b>熟练使用数据透视表、多维度交叉汇总、数据核对及基础可视化；熟悉增值税发票类型及企业付款审批流程。',
    '<b>统计分析：</b>熟练使用EViews、Stata，掌握描述性统计、回归分析及基础实证研究方法。具备校内教学与辅导经历，个人网站展示3段原创EViews教程。',
    '<b>AI工具：</b>熟悉ChatGPT等生成式AI工具及AI Agent工作方式，辅助数据清洗、统计分析、报告撰写及工作流程优化。',
]: story.append(p(text))

def footer(canvas, doc):
    canvas.setFont('Chinese', 7)
    canvas.setFillColor(muted)
    canvas.drawString(42, 29, '公开版简历｜金额、成本及重量以概数展示；不包含生日与手机号。')
    canvas.drawRightString(A4[0]-42, 29, str(doc.page))

out = ROOT / 'assets' / 'luodun-resume.pdf'
out.parent.mkdir(parents=True, exist_ok=True)
SimpleDocTemplate(str(out), pagesize=A4, leftMargin=42, rightMargin=42, topMargin=32, bottomMargin=46, title='罗顿 - 公开版求职简历', author='罗顿').build(story, onFirstPage=footer, onLaterPages=footer)
print(str(out))

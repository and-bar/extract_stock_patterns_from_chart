"""
Combination of keys:
    Escape - to quit the program
    move the wheel of the mouse to displacing history of the chart
    press '1' button to select next ticker to the start of the list of tickers
    press '2' button to select next ticker to the end of the list of tickers
    press 'c' button change chart in mode of candle or line
    click with left buton of the mouse dor first point of the line and second click with left buton of the mouse to draw the line
    
    
    Draws data from ndarray to the canvas.
    Displacing among the historical data using wheel of the mouse.
    Creates image with name of the ticker and writes it to the ndarray.
    Fills out all NaN values in pandas data frame.
    Draws lines of prices at the background of the chart. Can process till 15.000 $ in price of stock else rise error.
    Draws prices labels on the right side of the chart.
    Draw volumes.
    Draw chart in form of line on closes of bars.
    Draws lines on the chart with two clicks of the left button of the mouse.
    Draw SMA200 and SMA 50 on candlechart.
    Get data from Alpha Vantage.
    draw cross in vertical en horizontal line.
    Right button of the mouse saves two archives: one graphical of some range of bars and other pickle format with those data
        to C:\temp\patterns sell and buy.
    Button "arrow up" will name files with "buy" word in ther filename.
    Button "arrow down" will name files with "sell" word in ther filename.
       
TO DO:
    Plot date : first day of every month
    
"""
import talib
import time
import numpy as np
import tkinter as tki
#import sys
from PIL import Image, ImageTk, ImageFont, ImageDraw
#from iexfinance import get_historical_data
from alpha_vantage.timeseries import TimeSeries

alphavantagekey = input("Input your Alpha Vantage acces key:\n") 

ts = TimeSeries(key= alphavantagekey, output_format='pandas')

# set list of the symbols START
# ^GSPC - S&P 500 , ^DJI - Dow 30
# https://prediqtiv.github.io/alpha-vantage-cookbook/#https://rawgit.com/prediqtiv/alpha-vantage-cookbook/master/symbol-lists.md
# https://openfigi.com/search#!?simpleSearchString=msft&marketSector=Equity&page=1
# https://github.com/prediqtiv/alpha-vantage-cookbook/tree/master/symbol-search
# https://prediqtiv.github.io/alpha-vantage-cookbook/symbol-search/openfigi-api-front-end.html

# tickers = "BB   BBAX   BBBY   BBC   BBCA   BBCP   BBD   BBDC   BBDO   BBEU   BBF   BBGI   BBH   BBJP   BBK   BBL   BBN   BBP   BBRC   BBRE   BBSI   BBT   BBU   BBVA   BBW   BBX   BBY   BC   BCAC   BCACU   BCBP   BCC   BCD   BCE   BCEI   BCH   BCI   BCLI   BCM   BCNA   BCO   BCOM   BCOR   BCOV   BCPC   BCRH   BCRX   BCS   BCV   BCX   BDC   BDCL   BDCS   BDCZ   BDD   BDGE   BDJ   BDL   BDN   BDR   BDRY   BDSI   BDX   BDXA   BE   BEAT   BECN   BEDU   BEF   BEL   BELFA   BELFB   BEMO   BEN   BEP   BERN   BERY   BF-A   BF-B   BFAM   BFIN   BFIT   BFK   BFO   BFOR   BFR   BFRA   BFS   BFY   BFZ   BG   BGB   BGCP   BGFV   BGG   BGH   BGI   BGIO   BGNE   BGR   BGS   BGSF   BGT   BGX   BGY   BH   BHB   BHBK   BHC   BHE   BHF   BHGE   BHK   BHLB   BHP   BHR   BHTG   BHV   BHVN   BIB   BIBL   BICK   BID   BIDU   BIF   BIG   BIIB   BIKR   BIL   BILI   BIO   BIO-B   BIOC   BIOL   BIOS   BIP   BIS   BIT   BITA   BIV   BIZD   BJ   BJK   BJRI   BJUL   BK   BKC   BKCC   BKD   BKE   BKEP   BKEPP   BKF   BKH   BKI   BKJ   BKK   BKLN   BKN   BKNG   BKS   BKSC   BKT   BKTI   BKU   BKYI   BL   BLBD   BLCM   BLCN   BLD   BLDP   BLDR   BLE   BLES   BLFS   BLHY   BLIN   BLK   BLKB   BLL   BLMN   BLMT   BLNK   BLOK   BLPH   BLRX   BLUE   BLV   BLW   BLX   BMA   BMCH   BME   BMI   BMLP   BMO   BMRA   BMRC   BMRN   BMS   BMTC   BMY   BNCL   BND   BNDC   BNDX   BNED   BNFT   BNGO   BNO   BNS   BNSO   BNTC   BNY   BOCH   BOE   BOH   BOIL   BOJA   BOKF   BOLD   BOM   BOMN   BOND   BOOM   BOON   BOOT   BORN   BOSC   BOSS   BOTJ   BOTZ   BOUT   BOX   BOXL   BP   BPFH   BPI   BPL   BPMC   BPMP   BPMX   BPOP   BPR   BPRAP   BPT   BPTH   BPY   BQH   BR   BRAC   BRC   BREW   BRF   BRFS   BRG   BRID   BRK-A   BRK-B   BRKL   BRKR   BRKS   BRN   BRO   BRPA   BRQS   BRS   BRSS   BRT   BRX   BRY   BRZU   BSAC   BSBR   BSCJ   BSCK   BSCL   BSCM   BSCN   BSCO   BSCP   BSCQ   BSCR   BSCS   BSD   BSE   BSET   BSGM   BSIG   BSJJ   BSJK   BSJL   BSJM   BSJN   BSJO   BSJP   BSJQ   BSL   BSM   BSMX   BSQR   BSRR   BST   BSTC   BSTI   BSV   BSX   BT   BTA   BTAI   BTAL   BTE   BTEC   BTG   BTI   BTN   BTO   BTT   BTU   BTX   BTZ   BUD   BUI   BURG   BURL   BUSE   BUY   BUYN   BUZ   BV   BVAL   BVN   BVSN   BVXV   BW   BWA   BWEN   BWFG   BWG   BWL-A   BWMCU   BWX   BWXT   BWZ   BX   BXC   BXE   BXG   BXMT   BXMX   BXP   BXS   BY   BYD   BYFC   BYLD   BYM   BYSI   BZF   BZH   BZM   BZQ   BZUN   C   CAAP   CAAS   CABO   CAC   CACC   CACG   CACI   CADC   CADE   CAE   CAF   CAG   CAH   CAI   CAJ   CAKE   CAL   CALA   CALF   CALM   CALX   CAMP   CAMT   CANE   CANF   CANG   CAPE   CAPL   CAPR   CAR   CARA   CARB   CARG   CARO   CARS   CART   CARV   CARZ   CASA".split('   ')
tickers = "BB   BBAX   BBBY   BBC   BBCA   BBCP   BBD   BBDC   BBDO   BBEU   BBF   BBGI   BBH".split('   ')
# set list of the symbols END

# get financial data of the ticker and fill out all NaN in it START
def get_df_from_provider_of_financial_data_and_get_out_NaN (symbol, period, show_sma200 = False, show_sma50 = False, show_MACD = True, 
                                                            fastperiod_MACD = 12, slowperiod_MACD = 24, signalperiod_MACD = 9): # period: 1D, 
    if period == '1D':
        try: # if symbol do not exist in data provider data base on tickers
            df, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
            df.rename(columns={'1. open':'open', '2. high':'high', '3. low':'low', '4. close':'close', '5. volume':'volume'}, inplace=True)
            if df.isnull().any().any() == True: # if exist any NaN in the DF
                for row in ['open','high','low']:
                    df[row][df[row].isnull()] = df['close'][df[row].isnull()]  # fill nan values from the 'close' row
        except Exception:
            print("1D period. Can't get data on ticker : ", symbol)
    if period == '1M':
        try: # if symbol do not exist in data provider data base on tickers
            df, meta_data = ts.get_monthly(symbol=symbol)
            df.rename(columns={'1. open':'open', '2. high':'high', '3. low':'low', '4. close':'close', '5. volume':'volume'}, inplace=True)
            if df.isnull().any().any() == True: # if exist any NaN in the DF
                for row in ['open','high','low']:
                    df[row][df[row].isnull()] = df['close'][df[row].isnull()]  # fill nan values from the 'close' row
        except Exception:
            print("1M period. Can't get data on ticker : ", symbol)
    if period == '1W':
        try: # if symbol do not exist in data provider data base on tickers
            df, meta_data = ts.get_weekly(symbol=symbol)
            df.rename(columns={'1. open':'open', '2. high':'high', '3. low':'low', '4. close':'close', '5. volume':'volume'}, inplace=True)
            if df.isnull().any().any() == True: # if exist any NaN in the DF
                for row in ['open','high','low']:
                    df[row][df[row].isnull()] = df['close'][df[row].isnull()]  # fill nan values from the 'close' row
        except Exception:
            print("1W period. Can't get data on ticker : ", symbol)
    if period == '1min' or period == '5min' or period == '15min' or period == '30min' or period == '60min':
        try: # if symbol do not exist in data provider data base on tickers
            df, meta_data = ts.get_intraday(symbol=symbol, interval=period, outputsize='full')
            df.rename(columns={'1. open':'open', '2. high':'high', '3. low':'low', '4. close':'close', '5. volume':'volume'}, inplace=True)
            if df.isnull().any().any() == True: # if exist any NaN in the DF
                for row in ['open','high','low']:
                    df[row][df[row].isnull()] = df['close'][df[row].isnull()]  # fill nan values from the 'close' row
        except Exception:
            print(period + ' period. ' + "Can't get data on ticker : ", symbol)
    #preparing data for TA-lib START
    
    if show_sma200 == True:
        df['sma200'] = talib.SMA(df['close'].values, timeperiod=200)
    
    if show_sma50 == True:
        df['sma50'] = talib.SMA(df['close'].values, timeperiod=50)
    
    if show_MACD == True:
        macd = talib.MACD(real=df['close'].values, fastperiod=fastperiod_MACD, slowperiod=slowperiod_MACD, signalperiod=signalperiod_MACD)
        df['macd_fast'] = macd[0]
        df['macd_slow'] = macd[1]
        df['macd_signal'] = macd[2]
    
    #preparing data for TA-lib END
    return df
# get financial data of the ticker and fill out all NaN in it END

#import data frame START
symbol = tickers[0]
index_number_of_the_symbol_in_list_of_tickers = 0
period = '30min' # 1min, 5min, 15min, 30min, 60min
df = get_df_from_provider_of_financial_data_and_get_out_NaN (symbol, period, show_sma200=True, show_sma50=True, show_MACD=True)
#import data frame END

#create window START
window = tki.Tk()
window.attributes('-fullscreen', True)

# CLOSE WINDOW IF PRESSED ESC BUTTON - START
def close_window(event):
    
    window.quit()
    window.destroy()

window.bind("<Escape>", close_window) # press Control+Escape to quit the program
# CLOSE WINDOW IF PRESSED ESC BUTTON - END

# get resolution of the screen START 
# 4K 3840x2160
res_window_width = 1920 #3840
res_window_heigt = 440 #1005
candales_in_the_chart = int((res_window_width - 40)/3-15)
# get resolution of the screen END

# draw or not the cross on the chart START
draw_cross_on_chart = True
# draw or not the cross on the chart END

# set the height of chart for volume of the chart START
height_of_chart_for_volume = 50
width_of_chart_for_volume = res_window_width
# set the height of chart for volume of the chart END

# creating instance of canvas START
window_canvas = tki.Canvas(window, width=1920, height=1080)
window_canvas.pack()
# creating instance of canvas END

# forming ndarray from stock data START
def create_candle_chart_ndarray(stock_data_frame, dimension_of_ndarray, text_of_bottom_info_line):
    '''
    Creates  ndarray with candle chart given as input 600 candles maximum for 1440x900 resolution screen
    Candle chart 1359 pixels and 81 pixels blanc space right side
    DataFrame of stock given without NaN entrances of variables
    Draws level prices on the back front ores_window_heigt
    Draws at the bottom of chart volumes of every candle
    input variables:
        1) DataFrame of stock pandas format <= 600 registries
        2) Dimension for ndarray [height, width] in form of list
    output: ndarray chart array_prices_chart
    '''
    global array_prices_chart
    
    array_prices_chart = np.random.randint(0,1,(dimension_of_ndarray[0],dimension_of_ndarray[1],3),dtype='uint8')    
    array_prices_chart[:,:] = [255,255,204]
    
    range_of_stock_data_frame = stock_data_frame.shape[0] # creating variable for iterating thru the dataframe
    low_global_prices = stock_data_frame.low.min() # get minimum price on period of dataframe
    high_global_prices = stock_data_frame.high.max() # get maximum price on period of dataframe
    high_minus_low_global_prices = high_global_prices - low_global_prices # get difference between maximum and minimum price
    
    def text_max_4_symbols_to_ndarray (text):
        '''
        creates ndarray with text 10x40 dimension
        '''
        # creating ndarray image from text START
        font = ImageFont.truetype('arial.ttf', size=10) # Most fonts are located in /usr/share/fonts. in Ubuntu ; here 
        img_text=Image.new("RGB", size=(40,10),color=(255,255,204)) # 30 is width and 10 is high
        draw = ImageDraw.Draw(img_text)
        draw.text((0, 0), text,(0,0,0),font=font) # (0, 0) here the position of the text in the matrix
        # creating ndarray image from text END
        return np.array(img_text) # the selection where to pass the image with text
    
    def text_to_ndarray (text):
        '''
        creates ndarray with text
        '''
        # creating ndarray image from text START
        font = ImageFont.truetype('arial.ttf', size=20) # Most fonts are located in /usr/share/fonts. in Ubuntu ; here 
        img_text=Image.new("RGB", size=(dimension_of_ndarray[1],20),color=(255,255,204)) # 30 is width and 10 is high
        draw = ImageDraw.Draw(img_text)
        draw.text((0, -2), text,(0,0,0),font=font) # (0, 0) here the position of the text in the matrix
        # creating ndarray image from text END
        return np.array(img_text) # the selection where to pass the image with text
    
    # set resolution and create list of the levels of prices levels for background START
    if (high_global_prices - low_global_prices)/0.1 <= 30 : # true if difference between high_global_prices and low_global_prices <= 3 $
        all_prices_range = np.arange(low_global_prices,high_global_prices,0.1)
        all_prices_range = np.around(all_prices_range,decimals=1)
        list_of_prices_for_background_levels = np.array([])
        for i in all_prices_range:
            list_of_prices_for_background_levels = np.append(list_of_prices_for_background_levels, i)
    
    elif (high_global_prices - low_global_prices)/0.5 <= 30 :  # true if difference between high_global_prices and low_global_prices <= 15 $
        all_prices_range = np.arange(low_global_prices,high_global_prices,0.01)
        all_prices_range = np.around(all_prices_range,decimals=2)
        list_of_prices_for_background_levels = np.array([])
        for i in all_prices_range:
            if str(i).split('.')[1] == ('5') or str(i).split('.')[1] == ('0'):
                list_of_prices_for_background_levels = np.append(list_of_prices_for_background_levels, i)
    
    elif (high_global_prices - low_global_prices)/1 <= 30 :  # true if difference between high_global_prices and low_global_prices <= 30 $
        all_prices_range = np.arange(low_global_prices,high_global_prices,0.1)
        all_prices_range = np.around(all_prices_range,decimals=1)
        list_of_prices_for_background_levels = np.array([])
        for i in all_prices_range:
            if str(i).split('.')[1] == ('0'):
                list_of_prices_for_background_levels = np.append(list_of_prices_for_background_levels, i)
    
    elif (high_global_prices - low_global_prices)/5 <= 30 : # true if difference between high_global_prices and low_global_prices <= 150 $
        all_prices_range = np.arange(low_global_prices,high_global_prices)
        all_prices_range = all_prices_range/10
        all_prices_range = np.around(all_prices_range,decimals=1)
        list_of_prices_for_background_levels = np.array([])
        for i in all_prices_range:
            if str(i).split('.')[1] == ('5') or str(i).split('.')[1] == ('0'):
                list_of_prices_for_background_levels = np.append(list_of_prices_for_background_levels, i)
        list_of_prices_for_background_levels *= 10
        
    elif (high_global_prices - low_global_prices)/10 <= 30 : # true if difference between high_global_prices and low_global_prices <= 300 $
        all_prices_range = np.arange(low_global_prices,high_global_prices)
        all_prices_range = all_prices_range/10
        all_prices_range = np.around(all_prices_range,decimals=1)
        list_of_prices_for_background_levels = np.array([])
        for i in all_prices_range:
            if str(i).split('.')[1] == ('0'):
                list_of_prices_for_background_levels = np.append(list_of_prices_for_background_levels, i)
        list_of_prices_for_background_levels *= 10
    
    elif (high_global_prices - low_global_prices)/20 <= 30 : # true if difference between high_global_prices and low_global_prices <= 600 $
        all_prices_range = np.arange(low_global_prices,high_global_prices,10)
        all_prices_range = all_prices_range/100
        all_prices_range = np.around(all_prices_range,decimals=1)
        list_of_prices_for_background_levels = np.array([])
        for i in all_prices_range:
            if str(i).split('.')[1] == ('0') or str(i).split('.')[1] == ('2')  or str(i).split('.')[1] == ('4')  or str(i).split('.')[1] == ('6') or str(i).split('.')[1] == ('8'):
                list_of_prices_for_background_levels = np.append(list_of_prices_for_background_levels, i)
        list_of_prices_for_background_levels *= 100
    
    elif (high_global_prices - low_global_prices)/50 <= 30 : # true if difference between high_global_prices and low_global_prices <= 1candales_in_the_chart $
        all_prices_range = np.arange(low_global_prices,high_global_prices,10)
        all_prices_range = all_prices_range/100
        all_prices_range = np.around(all_prices_range,decimals=1)
        list_of_prices_for_background_levels = np.array([])
        for i in all_prices_range:
            if str(i).split('.')[1] == ('0') or str(i).split('.')[1] == ('5'):
                list_of_prices_for_background_levels = np.append(list_of_prices_for_background_levels, i)
        list_of_prices_for_background_levels *= 100
    
    elif (high_global_prices - low_global_prices)/100 <= 30 : # true if difference between high_global_prices and low_global_prices <= 3000 $
        all_prices_range = np.arange(low_global_prices,high_global_prices,10)
        all_prices_range = all_prices_range/100
        all_prices_range = np.around(all_prices_range,decimals=1)
        list_of_prices_for_background_levels = np.array([])
        for i in all_prices_range:
            if str(i).split('.')[1] == ('0'):
                list_of_prices_for_background_levels = np.append(list_of_prices_for_background_levels, i)
        list_of_prices_for_background_levels *= 100
    
    elif (high_global_prices - low_global_prices)/candales_in_the_chart <= 30 : # true if difference between high_global_prices and low_global_prices <= 1candales_in_the_chart0 $
        all_prices_range = np.arange(low_global_prices,high_global_prices,100)
        all_prices_range = all_prices_range/1000
        all_prices_range = np.around(all_prices_range,decimals=1)
        list_of_prices_for_background_levels = np.array([])
        for i in all_prices_range:
            if str(i).split('.')[1] == ('0') or str(i).split('.')[1] == ('5'):
                list_of_prices_for_background_levels = np.append(list_of_prices_for_background_levels, i)
        list_of_prices_for_background_levels *= 1000
    # set resolution and create list of the levels of prices levels for background END
    
    # draw line levels of the prices and the prices on the right side of the chart in the background of the chart START
    for i in list_of_prices_for_background_levels:
        # draw lines START      here arr_price are in pixels dimension
        if i - low_global_prices == 0:
            arr_price = int(dimension_of_ndarray[0] - (dimension_of_ndarray[0] * (i - low_global_prices + 0.001) / high_minus_low_global_prices))
            array_prices_chart[arr_price-2:arr_price-1, 0:res_window_width-43] = [220, 220, 175] # draw here price line
        else:
            arr_price = int(dimension_of_ndarray[0] - (dimension_of_ndarray[0] * (i - low_global_prices) / high_minus_low_global_prices))
            array_prices_chart[arr_price-1:arr_price, 0:res_window_width-43] = [220, 220, 175] # draw here price line
        # draw lines END
        
        # draw prices text START
        if i - low_global_prices > 0:
            if arr_price < 10: # if arr_price less than 10 pixels cant fit ndarray with price label to the ndarray candle chart
                arr_price = 10 # cant be less than 10 else rises error 'can't brodcast input array'
            elif arr_price > dimension_of_ndarray[0]-1: # the same as in the top but for the bottom of the chart
                   arr_price = dimension_of_ndarray[0]-1
            
            array_prices_chart[arr_price-10:arr_price,dimension_of_ndarray[1]-40:dimension_of_ndarray[1]] = text_max_4_symbols_to_ndarray (str(i)+'0') # draw on the chart ndarray with price label
    # draw line levels of the prices and the prices on the right side of the chart in the background of the chart END
    
    array_line_chart = array_prices_chart.copy()
    array_candle_chart = array_prices_chart.copy()
    
    # this block draws candles START
    for iterator_df in range(range_of_stock_data_frame): # iterate thru dataframe
    
        open_minus_global_low = stock_data_frame.open[iterator_df] - low_global_prices
        close_minus_global_low = stock_data_frame.close[iterator_df] - low_global_prices
    
        low_minus_global_low = stock_data_frame.low[iterator_df] - low_global_prices
        high_minus_global_low = stock_data_frame.high[iterator_df] - low_global_prices
    
        arr_bar_open = dimension_of_ndarray[0] * open_minus_global_low / high_minus_low_global_prices
        arr_bar_close = dimension_of_ndarray[0] * close_minus_global_low / high_minus_low_global_prices
    
        arr_bar_low = dimension_of_ndarray[0] * low_minus_global_low / high_minus_low_global_prices
        arr_bar_high = dimension_of_ndarray[0] * high_minus_global_low / high_minus_low_global_prices
    
        if stock_data_frame.close[iterator_df] < stock_data_frame.open[iterator_df]: # down price bearish
            #creates tails of the candle
            array_candle_chart[dimension_of_ndarray[0]-int(arr_bar_high):dimension_of_ndarray[0]-int(arr_bar_low),iterator_df*3+1:iterator_df*3+2] = [168,20,20]
            #creates body of the candle
            array_candle_chart[dimension_of_ndarray[0]-int(arr_bar_open):dimension_of_ndarray[0]-int(arr_bar_close),iterator_df*3:iterator_df*3+3] = [168,20,20] #draw 3 pixel bar
            array_candle_chart[dimension_of_ndarray[0]-int(arr_bar_open):dimension_of_ndarray[0]-int(arr_bar_close),iterator_df*3+1:iterator_df*3+2] = [252,63,63] #draw light center pixel of the bar
            #draw here body of the candle if open-close is less the 1 pixel
            if (int(arr_bar_open)-int(arr_bar_close)) == 0:
                array_candle_chart[dimension_of_ndarray[0]-int(arr_bar_open):dimension_of_ndarray[0]-int(arr_bar_close)+1,iterator_df*3:iterator_df*3+3] = [168,20,20] #draw 3 pixel bar
        else: # up price bullish
            #creates tails of the candle
            array_candle_chart[dimension_of_ndarray[0]-int(arr_bar_high):dimension_of_ndarray[0]-int(arr_bar_low),iterator_df*3+1:iterator_df*3+2] = [10,48,10]
            #creates body of the candle
            array_candle_chart[dimension_of_ndarray[0]-int(arr_bar_close):dimension_of_ndarray[0]-int(arr_bar_open),iterator_df*3:iterator_df*3+3] = [10,48,10]  #draw 3 pixel bar
            array_candle_chart[dimension_of_ndarray[0]-int(arr_bar_close):dimension_of_ndarray[0]-int(arr_bar_open),iterator_df*3+1:iterator_df*3+2] = [31,148,31]  #draw light center pixel of the bar
            #draw here body of the candle if close-open is less the 1 pixel
            if (int(arr_bar_close)-int(arr_bar_open)) ==0:
                array_candle_chart[dimension_of_ndarray[0]-int(arr_bar_close):dimension_of_ndarray[0]-int(arr_bar_open)+1,iterator_df*3:iterator_df*3+3] = [10,48,10]  #draw 3 pixel bar
    # this block draws candles END
    
    # this block draws line chart START
    image_for_imagedraw = Image.fromarray(array_line_chart, mode='RGB')
    imagedraw_array_prices_chart = ImageDraw.Draw(image_for_imagedraw) # pass ndarray in ImageDraw.Draw object for drawing lines
    for iterator_df in range(range_of_stock_data_frame - 1): # iterate thru dataframe
        first_candle_close_minus_global_low = stock_data_frame.close[iterator_df] - low_global_prices
        second_candle_close_minus_global_low = stock_data_frame.close[iterator_df + 1] - low_global_prices
        first_candle_arr_bar_close = dimension_of_ndarray[0] - (int(dimension_of_ndarray[0] * first_candle_close_minus_global_low / high_minus_low_global_prices)) # height in pixels
        second_candle_arr_bar_close = dimension_of_ndarray[0] - (int(dimension_of_ndarray[0] * second_candle_close_minus_global_low / high_minus_low_global_prices)) # height in pixels
        imagedraw_array_prices_chart.line((iterator_df*3+1, first_candle_arr_bar_close, iterator_df*3+4, second_candle_arr_bar_close), fill=0, width=1)
    array_line_chart = np.asarray(image_for_imagedraw)
    # this block draws line chart END
    
    if 'sma200' in list(df):
        #draw SMA 200 START
        image_for_imagedraw = Image.fromarray(array_candle_chart, mode='RGB')
        imagedraw_array_prices_chart = ImageDraw.Draw(image_for_imagedraw) # pass ndarray in ImageDraw.Draw object for drawing lines
        for iterator_df in range(range_of_stock_data_frame - 1): # iterate thru dataframe
            if not np.isnan(stock_data_frame['sma200'][iterator_df]): #if variable are not NaN
                first_candle_SMA200_minus_global_low = stock_data_frame['sma200'][iterator_df] - low_global_prices
                second_candle_SMA200_minus_global_low = stock_data_frame['sma200'][iterator_df + 1] - low_global_prices
                first_candle_arr_bar_SMA200 = dimension_of_ndarray[0] - (int(dimension_of_ndarray[0] * first_candle_SMA200_minus_global_low / high_minus_low_global_prices)) # height in pixels
                second_candle_arr_bar_SMA200 = dimension_of_ndarray[0] - (int(dimension_of_ndarray[0] * second_candle_SMA200_minus_global_low / high_minus_low_global_prices)) # height in pixels
                imagedraw_array_prices_chart.line((iterator_df*3, first_candle_arr_bar_SMA200, iterator_df*3+3, second_candle_arr_bar_SMA200), fill=(255,0,0), width=2)
        array_candle_chart = np.asarray(image_for_imagedraw)
        #draw SMA 200 END
    
    if 'sma50' in list(df):   
        #draw SMA 50 START
        image_for_imagedraw = Image.fromarray(array_candle_chart, mode='RGB')
        imagedraw_array_prices_chart = ImageDraw.Draw(image_for_imagedraw) # pass ndarray in ImageDraw.Draw object for drawing lines
        for iterator_df in range(range_of_stock_data_frame - 1): # iterate thru dataframe
            if not np.isnan(stock_data_frame['sma50'][iterator_df]): #if variable are not NaN
                first_candle_SMA50_minus_global_low = stock_data_frame['sma50'][iterator_df] - low_global_prices
                second_candle_SMA50_minus_global_low = stock_data_frame['sma50'][iterator_df + 1] - low_global_prices
                first_candle_arr_bar_SMA50 = dimension_of_ndarray[0] - (int(dimension_of_ndarray[0] * first_candle_SMA50_minus_global_low / high_minus_low_global_prices)) # height in pixels
                second_candle_arr_bar_SMA50 = dimension_of_ndarray[0] - (int(dimension_of_ndarray[0] * second_candle_SMA50_minus_global_low / high_minus_low_global_prices)) # height in pixels
                imagedraw_array_prices_chart.line((iterator_df*3, first_candle_arr_bar_SMA50, iterator_df*3+3, second_candle_arr_bar_SMA50), fill=(0,0,255), width=2)
        array_candle_chart = np.asarray(image_for_imagedraw)
        #draw SMA 50 END
    
    if 'macd_fast' in list(df):
        #draw MACD chart START
        height_of_chart_for_MACD = 200
        array_MACD_chart =  np.random.randint(0,1,(height_of_chart_for_MACD, dimension_of_ndarray[1],3),dtype='uint8')    
        array_MACD_chart[:] = [255,255,204]
        
        low_global_MACD = min([stock_data_frame['macd_fast'].min(), stock_data_frame['macd_slow'].min(), stock_data_frame['macd_signal'].min()])
        high_global_MACD = max([stock_data_frame['macd_fast'].max(), stock_data_frame['macd_slow'].max(), stock_data_frame['macd_signal'].max()])
        high_minus_low_global_digits_for_MACD = high_global_MACD - (low_global_MACD)
        
        zero_line_of_MACD_chart_minus_global_low = abs(low_global_MACD - (0))
        zero_line_of_MACD_chart = height_of_chart_for_MACD - (int(height_of_chart_for_MACD * zero_line_of_MACD_chart_minus_global_low / high_minus_low_global_digits_for_MACD)) # height in pixels
        
        array_MACD_chart[zero_line_of_MACD_chart:zero_line_of_MACD_chart+1 , :-43] = [194,201,0] # draw here middle line separator of MACD chart
        
        array_MACD_chart[zero_line_of_MACD_chart-5:zero_line_of_MACD_chart+5 , -40:] = text_max_4_symbols_to_ndarray('0.00')
        #array_MACD_chart[zero_line_of_MACD_chart+20:zero_line_of_MACD_chart+30 , -40:] = text_max_4_symbols_to_ndarray('MACD')
        array_MACD_chart[10:20 , -40:] = text_max_4_symbols_to_ndarray('MACD')
        
        image_for_imagedraw = Image.fromarray(array_MACD_chart, mode='RGB')
        imagedraw_array_MACD_chart = ImageDraw.Draw(image_for_imagedraw) # pass ndarray in ImageDraw.Draw object for drawing lines
        
        colors_of_lines_MACD = [(0,0,204), (102,204,0), (255,0,0)]
        for iterator_df in range(range_of_stock_data_frame - 1): # iterate thru dataframe
            #if df.isnull().any().any() == True:
            if not np.isnan(stock_data_frame['macd_fast'][iterator_df]): #if variable are not NaN
                iterator_of_colors_MACD = -1
                for type_of_signal_MACD in [stock_data_frame['macd_fast'], stock_data_frame['macd_slow'], stock_data_frame['macd_signal']]: # stock_data_frame['macd_slow'], stock_data_frame['macd_signal']
                    iterator_of_colors_MACD += 1
                    if type_of_signal_MACD[iterator_df] <= 0:
                        first_coordinate__MACD_minus_global_low = abs(low_global_MACD - (type_of_signal_MACD[iterator_df]))
                        second_coordinate__MACD_minus_global_low = abs(low_global_MACD - (type_of_signal_MACD[iterator_df + 1]))
                    else:
                        first_coordinate__MACD_minus_global_low = abs(low_global_MACD) + (type_of_signal_MACD[iterator_df])
                        second_coordinate__MACD_minus_global_low = abs(low_global_MACD) + (type_of_signal_MACD[iterator_df + 1])
                    #print('first_coordinate__MACD_minus_global_low = ', first_coordinate__MACD_minus_global_low )
                    
                    first_coordinate__MACD = height_of_chart_for_MACD - (int(height_of_chart_for_MACD * first_coordinate__MACD_minus_global_low / high_minus_low_global_digits_for_MACD)) # height in pixels
                    second_coordinate__MACD = height_of_chart_for_MACD - (int(height_of_chart_for_MACD * second_coordinate__MACD_minus_global_low / high_minus_low_global_digits_for_MACD)) # height in pixels
                    
                    color_of_signal_line_MACD = colors_of_lines_MACD[iterator_of_colors_MACD]
                    imagedraw_array_MACD_chart.line((iterator_df*3, first_coordinate__MACD, iterator_df*3+3, second_coordinate__MACD), fill=color_of_signal_line_MACD, width=2)
        array_MACD_chart = np.asarray(image_for_imagedraw)
        #draw MACD chart END
    
    # this block creates volume chart START
    array_volumes_chart =  np.random.randint(0,1,(height_of_chart_for_volume, dimension_of_ndarray[1],3),dtype='uint8')    
    array_volumes_chart[:,:] = [255,255,204]
    low_global_volume = stock_data_frame['volume'].min() # get minimum price on period of dataframe
    high_global_volume = stock_data_frame['volume'].max() # get maximum price on period of dataframe
    high_minus_low_global_volumes = high_global_volume - low_global_volume # get difference between maximum and minimum volume
    height_in_pixels_of_maximum_volume_bar = height_of_chart_for_volume - 10
        
    range_of_volumes = np.linspace(low_global_volume, high_global_volume, 5) # creating list of range of volumes
    
    # function creating labels for volumes START
    def get_label_volume_short_version (volume_bar):
        if volume_bar < 900:
            label_volume_string = str(round(volume_bar, 1))
        if volume_bar < 900000 and volume_bar >= 900:
            label_volume_string = str(round(volume_bar/1000, 1)) + ' k'
        if volume_bar < 900000000 and volume_bar >= 900000:
            label_volume_string = str(round(volume_bar/1000000, 1)) + ' M'
        if volume_bar < 900000000000 and volume_bar >= 900000000:
            label_volume_string = str(round(volume_bar/1000000000, 1)) + ' B'
        return label_volume_string
    # function creating labels for volumes END
    
    # drawing volume lines and labels START
    for iterator_volumes in range_of_volumes:
        volume_line = int((iterator_volumes - low_global_volume) * height_in_pixels_of_maximum_volume_bar / high_minus_low_global_volumes)
        if volume_line < 1:
            volume_line = 1
        array_volumes_chart[height_of_chart_for_volume - volume_line - 2: height_of_chart_for_volume - volume_line - 1, : dimension_of_ndarray[1]-43] = [230, 184, 0] # draw here volume line
        array_volumes_chart[height_of_chart_for_volume - volume_line - 10: height_of_chart_for_volume - volume_line, dimension_of_ndarray[1]-40:dimension_of_ndarray[1]] = text_max_4_symbols_to_ndarray (get_label_volume_short_version(iterator_volumes)) # create label for max volume
    # drawing volume lines and labels END
    
    # creating volumes bars START
    for iterator_volume in range(range_of_stock_data_frame): # iterate thru dataframe
        iterator_volume_in_pixels = (stock_data_frame['volume'][iterator_volume] - low_global_volume) * height_in_pixels_of_maximum_volume_bar / high_minus_low_global_volumes
        if iterator_volume_in_pixels < 1 :
            iterator_volume_in_pixels = 1
        array_volumes_chart[height_of_chart_for_volume - int(iterator_volume_in_pixels) - 2: height_of_chart_for_volume - 2, iterator_volume*3+1:iterator_volume*3+2] = [0,0,0]
    # creating volumes bars END
    
    # this block creates volume chart END
    
    # creating separation between chart START
    horizontal_line_divider_of_charts = np.random.randint(0,1,(10,dimension_of_ndarray[1],3),dtype='uint8')
    horizontal_line_divider_of_charts[:,:] = [255,255,204]
    horizontal_line_divider_of_charts[5:6,:] = [0,0,0]
    # creating separation between chart End
    
    # creatin ifotext array START
    
    # creatin ifotext array END
    
    # concatenating candle and volume chart and give it for return
    array_prices_chart = np.vstack((array_candle_chart, horizontal_line_divider_of_charts, array_MACD_chart, horizontal_line_divider_of_charts, array_line_chart, 
                                    horizontal_line_divider_of_charts, array_volumes_chart, text_to_ndarray(text_of_bottom_info_line)))
    
    return array_prices_chart
# forming ndarray from stock data END

# Function that calls create_candle_chart_array and draws it to the canvas START
def draw_ndarray_to_the_canvas(stock_data_frame, dimensions_of_ndarray):
    '''
    Calls create_candle_chart_ndarray and draws ndarray to the canvas
    input variables:
        1) DataFrame - stock_data_frame
        2) Dimensions for ndarray [height, width] in form of list
    Creates the name of the ticker and draws it to the ndarray
    '''
    array = create_candle_chart_ndarray(stock_data_frame,dimensions_of_ndarray, ('   symbol: ' + symbol + '   timeframe: ' + period)) 
    #Image.fromarray(array).save('array.png')
    
    # draw image to the canvas START
    image = Image.fromarray(array, mode='RGB')
    image = ImageTk.PhotoImage(image)
    window_canvas.create_image((0,0),image= image, anchor=tki.NW) #anchor=window.NW 
    window_canvas.image = image # creating image for if function run till the end not desapeared image on canvas
    window_canvas.update()
    # draw image to the canvas END
    
# Function that calls create_candle_chart_array and draws it to the canvas END

# writing ndarry to the canvas START
df_start_bar = df.shape[0]-candales_in_the_chart #reference for start bar for DataFrame for 1440x900 screen resolution
df_end_bar = df.shape[0] #reference for end bar for DataFrame
draw_ndarray_to_the_canvas(df[df_start_bar:df_end_bar],[res_window_heigt - height_of_chart_for_volume,res_window_width])
# writing ndarry to the canvas END

# function redraw the canvas if wheel of the mouse turned START
step_in_bars = 50 # step for desplacing the bars among the DataFrame for forming ndarray
def mouse_wheel(event):
    '''
    If wheel of the mouse turned up or down, redraw the chart with displacement
    '''
    global df_start_bar  #reference for start bar for DataFrame
    global df_end_bar #reference for end bar for DataFrame
    if event.num == 5 or event.delta == -120: # wheel turned down   if event.num == -120:
        if (df_start_bar-step_in_bars) >= 0: # not the left end of the chart
            df_start_bar-=step_in_bars
            df_end_bar-=step_in_bars
            draw_ndarray_to_the_canvas(df[df_start_bar:df_end_bar],[res_window_heigt - height_of_chart_for_volume,res_window_width])
        else:
            if df_start_bar != 0:
                df_start_bar = 0
                df_end_bar = candales_in_the_chart
                draw_ndarray_to_the_canvas(df[df_start_bar:df_end_bar],[res_window_heigt - height_of_chart_for_volume,res_window_width])
    if event.num == 4 or event.delta == 120: # wheel turned up
        if (df_end_bar+step_in_bars) <= df.shape[0]: # not the right end of the chart
            df_start_bar+=step_in_bars
            df_end_bar+=step_in_bars
            draw_ndarray_to_the_canvas(df[df_start_bar:df_end_bar],[res_window_heigt - height_of_chart_for_volume,res_window_width])    
        else:
            if df_end_bar != df.shape[0]:
                df_start_bar = df.shape[0]-candales_in_the_chart
                df_end_bar = df.shape[0]
                draw_ndarray_to_the_canvas(df[df_start_bar:df_end_bar],[res_window_heigt - height_of_chart_for_volume,res_window_width])
# function redraw the canvas if wheel of the mouse turned END

# save df pattern for sell or buy class press up and down button START
string_sell_or_buy = 'sell '

def arrow_down(event):
    global string_sell_or_buy
    string_sell_or_buy = 'sell '
def arrow_up(event):
    global string_sell_or_buy
    string_sell_or_buy = 'buy '

window.bind('<Down>', arrow_down)
window.bind('<Up>', arrow_up)
# save df pattern for sell or buy class pressin up and down button END

# change symbol next symbol  START
def event_button_2 (event):
    global index_number_of_the_symbol_in_list_of_tickers
    global symbol
    global df_start_bar
    global df_end_bar
    global df
    if index_number_of_the_symbol_in_list_of_tickers < len(tickers)-1: # if not the last ticker on the right side
        index_number_of_the_symbol_in_list_of_tickers+=1
        symbol = tickers[index_number_of_the_symbol_in_list_of_tickers]
        df = get_df_from_provider_of_financial_data_and_get_out_NaN (symbol, period, show_sma200=True, show_sma50=True)
        if df.shape[0] < candales_in_the_chart: # if the df.shape[0] is less than 600
            df_start_bar = 0
            df_end_bar = df.shape[0]
        else:
            df_start_bar = df.shape[0]-candales_in_the_chart #reference for start bar for DataFrame for 1440x900 screen resolution
            df_end_bar = df.shape[0] #reference for end bar for DataFrame
        draw_ndarray_to_the_canvas(df[df_start_bar:df_end_bar],[res_window_heigt - height_of_chart_for_volume,res_window_width])
window.bind("2", event_button_2) # press Control+Escape to quit the program
# change symbol next symbol END

# change symbol before symbol  START
def event_button_1 (event):
    global index_number_of_the_symbol_in_list_of_tickers
    global symbol
    global df_start_bar
    global df_end_bar
    global df
    if index_number_of_the_symbol_in_list_of_tickers > 0: # if not the first ticker in the list of the tickers
        index_number_of_the_symbol_in_list_of_tickers-=1
        symbol = tickers[index_number_of_the_symbol_in_list_of_tickers]
        df = get_df_from_provider_of_financial_data_and_get_out_NaN (symbol, period, show_sma200=True, show_sma50=True)
        if df.shape[0] < candales_in_the_chart:  # if the df.shape[0] is less than 600
            df_start_bar = 0
            df_end_bar = df.shape[0]
        else:
            df_start_bar = df.shape[0]-candales_in_the_chart #reference for start bar for DataFrame for 1440x900 screen resolution
            df_end_bar = df.shape[0] #reference for end bar for DataFrame
        draw_ndarray_to_the_canvas(df[df_start_bar:df_end_bar],[res_window_heigt - height_of_chart_for_volume,res_window_width])
window.bind("1", event_button_1) # press Control+Escape to quit the program
# change symbol before symbol  ENDleft

window.bind("<MouseWheel>", mouse_wheel) # wheel of the mouse event
window.bind("<MouseWheel>", mouse_wheel) # wheel of the mouse event

# left click of the mouse button START
left_button_first_click = False # activating the procedure of drawing the line on the chart
x_position_mouse_for_line_draw = 0
y_position_mouse_for_line_draw = 0

def draw_line_support_resistance_on_array_prices_chart (event):
    '''
    doing click on left button of the mouse get position x,y of the mouse on monitor, that position will be first point of the line
    and drawing line on array_prices_chart_for_drawing, the second point of the line will be current position
    x,y of the line. 
    '''
    global left_button_first_click
    global x_position_mouse_for_line_draw
    global y_position_mouse_for_line_draw
    global time_wait_200_miliseconds_for_drawing_line
    global array_prices_chart
    global array_temporal_prices_chart
    
    if left_button_first_click == False: # first click of the first button of the mouse
        left_button_first_click = True
        x_position_mouse_for_line_draw = event.x - 2# ndarray column 1 dimension
        y_position_mouse_for_line_draw = event.y - 2# ndarray row 0 dimension
        time_wait_200_miliseconds_for_drawing_line = time.time() * 1000 # in seconds, this variable + 0.2 of the seconds to draw a new line of support or resistance
    else: # second click of the first button of the mouse
        left_button_first_click = False
        array_prices_chart = array_temporal_prices_chart
        
        
window.bind("<Button-1>", draw_line_support_resistance_on_array_prices_chart)
# left click of the mouse button END

# event motion of the mouse for drawing lines of support and resistance START
#time_wait_200_miliseconds_for_drawing_line = time.time() * 1000 # in seconds, this variable + 0.003 of the seconds to draw a new line of support or resistance
def motion_mouse_event (event):
    
    global array_prices_chart
    global array_temporal_prices_chart
    global left_button_first_click
    global time_wait_200_miliseconds_for_drawing_line
    global draw_cross_on_chart
    
    if draw_cross_on_chart == True and left_button_first_click == False:
        
        array_temporal_prices_chart = array_prices_chart # to save the principal ndarray
        image_for_imagedraw = Image.fromarray(array_temporal_prices_chart, mode='RGB')
        imagedraw_array_prices_chart = ImageDraw.Draw(image_for_imagedraw) # pass ndarray in ImageDraw.Draw object for drawing lines
        imagedraw_array_prices_chart.line((0, event.y-2, res_window_width - 40, event.y-2), fill=0, width=1) # draw here horizontal line of the cross
        imagedraw_array_prices_chart.line((event.x - 200*3, event.y+4, event.x, event.y+4), fill=255, width=1) # draw here line of the lenght of selected range of bars for saving patterns
        imagedraw_array_prices_chart.line((event.x-2, 0, event.x-2, 2160), fill=0, width=1) # draw here vertical line of the cross
        
        array_temporal_prices_chart = np.asarray(image_for_imagedraw)
        
        # draw image to the canvas START
        image = Image.fromarray(array_temporal_prices_chart, mode='RGB')
        image = ImageTk.PhotoImage(image)
        window_canvas.create_image((1,1), image= image, anchor=tki.NW) #anchor=window.NW 
        window_canvas.image = image # creating image for if function run till the end not desapeared image on canvas
        window_canvas.update()
        # draw image to the canvas END
    
    if left_button_first_click == True: # clicked first time first button of the  mouse for drawing line
        
        if (time.time() * 1000) - time_wait_200_miliseconds_for_drawing_line >= 0.01: # draw lines if passed more than some time befor previous draw of the line
            
            array_temporal_prices_chart = array_prices_chart # to save the principal ndarray
            image_for_imagedraw = Image.fromarray(array_temporal_prices_chart, mode='RGB')
            imagedraw_array_prices_chart = ImageDraw.Draw(image_for_imagedraw) # pass ndarray in ImageDraw.Draw object for drawing lines
            
            imagedraw_array_prices_chart.line((x_position_mouse_for_line_draw, y_position_mouse_for_line_draw, event.x, event.y), fill=0, width=1)
            array_temporal_prices_chart = np.asarray(image_for_imagedraw)
            
            time_wait_200_miliseconds_for_drawing_line = time.time() * 1000
            
            # draw image to the canvas START
            image = Image.fromarray(array_temporal_prices_chart, mode='RGB')
            image = ImageTk.PhotoImage(image)
            window_canvas.create_image((1,1), image= image, anchor=tki.NW) #anchor=window.NW 
            window_canvas.image = image # creating image for if function run till the end not desapeared image on canvas
            window_canvas.update()
            # draw image to the canvas END

window.bind('<Motion>', motion_mouse_event)
# event moution of the mouse for drawing lines of support and resistance END

large_of_pattern_in_bars = 200 # numbers of bars that wiil save with pattern
list_patterns = []

# function for extracting data of patterns and add it to a list of patterns for DL START
def add_pattern_to_data_for_DL (event):
    
    global stock_data_frame
    global df
    global array_prices_chart
    
    number_of_the_bar_clicked_on_chart = int(event.x/3) # here number of bar on the cart
    
    if number_of_the_bar_clicked_on_chart >= large_of_pattern_in_bars:
        stock_data_frame = df[df_start_bar:df_end_bar]
        stock_pattern_pandas_frame = stock_data_frame[number_of_the_bar_clicked_on_chart - large_of_pattern_in_bars : number_of_the_bar_clicked_on_chart]
        list_patterns.append(stock_pattern_pandas_frame)
        
        # save image of pattern to a png file START
        array_prices_chart_copy = array_prices_chart.copy()
        
        text_for_pattern = '   symbol: ' + symbol + '   timeframe: ' + period
        array_of_pattern = create_candle_chart_ndarray(stock_pattern_pandas_frame, [300, stock_pattern_pandas_frame.shape[0]*3 + 50], text_of_bottom_info_line=text_for_pattern )
        image_of_pattern = Image.fromarray(array_of_pattern,'RGB')
        random_digit_str = str(np.random.randint(0,100000))
        image_of_pattern.save('C:/Temp/patterns sell and buy/'+ string_sell_or_buy + period + '_' + symbol + '_' + random_digit_str +'.png')
        
        array_prices_chart = array_prices_chart_copy.copy()
        # save image of pattern to a png file END
        
        # save dataframe figure to the file START
        
        # https://ianlondon.github.io/blog/pickling-basics/
        stock_pattern_pandas_frame.to_pickle('C:/Temp/patterns sell and buy/'+ string_sell_or_buy + period + '_' + symbol + '_' + random_digit_str +'.pickle')
        # use pandas.read_pickle('my_df.pickle') to read object from the pickle file
        
        
        # save dataframe figure to the file END
        
        '''
        # add selected pattern to the right of window START
        
        right_part_of_the_window_for_pattern = np.random.randint(0,1,(array_prices_chart.shape[0], res_with_right_part_window_for_the_pattern, 3),dtype='uint8')
        right_part_of_the_window_for_pattern[:,:] = [255,255,204]
        
        array_prices_chart = np.hstack((array_prices_chart,right_part_of_the_window_for_pattern))
        
        array_prices_chart[ 20 : 20 + array_of_pattern.shape[0] , res_window_width + 20 : res_window_width + 20 + array_of_pattern.shape[1] ] = array_of_pattern
        
        
        
        # add selected pattern to the right of window END
        '''
    else:
        print('number_of_the_bar_clicked_on_chart: ', number_of_the_bar_clicked_on_chart, 'less then 400 cant copy pattern    -     ', symbol)
        
# function for extracting data of patterns and add it to a list of patterns for DL END

# right click of the mouse button START
window.bind("<Button-3>", add_pattern_to_data_for_DL)
# right click of the mouse button END


window.mainloop()
#create window END














































































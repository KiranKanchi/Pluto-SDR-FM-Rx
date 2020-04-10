#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM_RX
# Author: KiranKanchi
# Generated: Sun Mar 29 01:22:03 2020
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class fm_receiver(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="FM_RX")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.tuner = tuner = 92.7e6
        self.samp_rate = samp_rate = 2e6
        self.rf_gain = rf_gain = 15
        self.down_rate = down_rate = 250e3
        self.Volume = Volume = 0

        ##################################################
        # Blocks
        ##################################################
        self._tuner_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.tuner,
        	callback=self.set_tuner,
        	label='Station select',
        	choices=[91.1e6, 91.9e6, 92.7e6, 93.5e6, 94.3e6, 98.3e6],
        	labels=[1,2,3,4,5,6],
        	style=wx.RA_HORIZONTAL,
        )
        self.Add(self._tuner_chooser)
        _rf_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rf_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	label='RF Gain',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._rf_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	minimum=10,
        	maximum=70,
        	num_steps=12,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.GridAdd(_rf_gain_sizer, 1, 0, 1, 4)
        _Volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._Volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_Volume_sizer,
        	value=self.Volume,
        	callback=self.set_Volume,
        	label='Volume',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._Volume_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_Volume_sizer,
        	value=self.Volume,
        	callback=self.set_Volume,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_Volume_sizer, 1, 5, 1, 8)
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=down_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Decimate_out',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_1.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=tuner,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Sampling bandpass',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.pluto_source_0 = iio.pluto_source('', int(tuner), int(samp_rate), int(20000000), 0x8000, True, True, True, "manual", rf_gain, '', True)
        self.low_pass_filter_0 = filter.fir_filter_ccf(int(samp_rate/down_rate), firdes.low_pass(
        	2, samp_rate, 100e3, 10e3, firdes.WIN_KAISER, 6.76))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((Volume/100, ))
        self.audio_sink_1 = audio.sink(24000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=down_rate,
        	audio_decimation=1,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.wxgui_fftsink2_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.pluto_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.pluto_source_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))

    def get_tuner(self):
        return self.tuner

    def set_tuner(self, tuner):
        self.tuner = tuner
        self._tuner_chooser.set_value(self.tuner)
        self.wxgui_fftsink2_0.set_baseband_freq(self.tuner)
        self.pluto_source_0.set_params(int(self.tuner), int(self.samp_rate), int(20000000), True, True, True, "manual", self.rf_gain, '', True)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.pluto_source_0.set_params(int(self.tuner), int(self.samp_rate), int(20000000), True, True, True, "manual", self.rf_gain, '', True)
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, 100e3, 10e3, firdes.WIN_KAISER, 6.76))

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self._rf_gain_slider.set_value(self.rf_gain)
        self._rf_gain_text_box.set_value(self.rf_gain)
        self.pluto_source_0.set_params(int(self.tuner), int(self.samp_rate), int(20000000), True, True, True, "manual", self.rf_gain, '', True)

    def get_down_rate(self):
        return self.down_rate

    def set_down_rate(self, down_rate):
        self.down_rate = down_rate
        self.wxgui_fftsink2_1.set_sample_rate(self.down_rate)

    def get_Volume(self):
        return self.Volume

    def set_Volume(self, Volume):
        self.Volume = Volume
        self._Volume_slider.set_value(self.Volume)
        self._Volume_text_box.set_value(self.Volume)
        self.blocks_multiply_const_vxx_0.set_k((self.Volume/100, ))


def main(top_block_cls=fm_receiver, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()

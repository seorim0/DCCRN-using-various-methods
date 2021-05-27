"""
Configuration for train_interface

You can check the essential information,
and if you want to change model structure or training method,
you have to change this file.
"""
#######################################################################
#                                 path                                #
#######################################################################
job_dir = './job/'
logs_dir = './logs/'
chkpt_model = None
chkpt = str(90)
if chkpt_model:
    chkpt_path = job_dir + chkpt_model + 'chkpt_' + chkpt + '.pt'

#######################################################################
#                         possible setting                            #
#######################################################################
# the list you can do
model_list = ['DCCRN']  # ['cCRN', 'DCUNET', 'DCCRN']
loss_list = ['MSE', 'SDR', 'SI-SNR', 'SI-SDR']
perceptual_list = ['False', 'LMS', 'PMSQE']
lstm_type = ['real', 'complex']
batch_type = ['real', 'complex']
mask_type = ['Direct(None make)', 'E', 'C', 'R']
window_type = ['hanning']

# experiment number setting
expr_num = ''
#######################################################################
#                           current setting                           #
#######################################################################
model = model_list[0]
cycle = False  # for Cyclic model
loss = loss_list[0]
perceptual = perceptual_list[0]
lstm = lstm_type[1]
batch_norm = batch_type[0]

masking_mode = mask_type[0]
window = window_type[0]

# hyper-parameters
max_epochs = 120
learning_rate = 0.001
batch = 6

# kernel size
dccrn_kernel_num = [32, 64, 128, 256, 256, 256]
dcunet_kernel_num = [72, 72, 144, 144, 144, 160, 160, 180]
#######################################################################
#                         model information                           #
#######################################################################
fs = 16000
win_len = 400
win_inc = 100
ola_ratio = win_inc / win_len
fft_len = 512
sam_sec = fft_len / fs
frm_samp = fs * (fft_len / fs)

rnn_layers = 2
rnn_units = 256

#######################################################################
#                      setting error check                            #
#######################################################################
# if the setting is wrong, print error message

#######################################################################
#                           print setting                             #
#######################################################################
print('--------------------  C  O  N  F  I  G  ----------------------')
print('--------------------------------------------------------------')
print('MODEL INFO : {}'.format(model))
print('LOSS INFO : {}, perceptual : {}'.format(loss, perceptual))
print('LSTM : {}'.format(lstm))
print('BATCH NORM : {}'.format(batch_norm))
print('CYCLE : {}'.format(cycle))
print('MASKING INFO : {}'.format(masking_mode))
print('\nBATCH : {}'.format(batch))
print('LEARNING RATE : {}'.format(learning_rate))
print('--------------------------------------------------------------')
print('--------------------------------------------------------------\n')
import numpy as np
from tensorboardX import SummaryWriter


writer = SummaryWriter(log_dir='./runTensorboard')


for epoch in range(100):
    writer.add_scalar('Sin_value', np.sin(epoch), epoch)
    writer.add_scalars('scalars_test', {'xsinx': epoch * np.sin(epoch), 'xcosx': epoch * np.cos(epoch)}, epoch)

writer.close()

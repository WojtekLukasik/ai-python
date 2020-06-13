import torch
import torch.nn.functional as F
from nn_model import Net
from torch import nn, optim
from torchvision import datasets, transforms

n_epochs = 3
batch_size_train = 64
batch_size_test = 1000
model = Net()
print("Model loaded.")
optimizer = optim.SGD(model.parameters(), lr=0.003, momentum=0.5)
criterion = nn.NLLLoss()

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.1307,), (0.3081,)),
                                ])

train_set = datasets.MNIST('PATH_TO_STORE_TRAIN_SET', download=True, train=True, transform=transform)
test_set = datasets.MNIST('PATH_TO_STORE_TEST_SET', download=True, train=False, transform=transform)
train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size_train, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_set, batch_size=batch_size_test, shuffle=True)

print("Data sets loaded.")

train_losses = []
train_counter = []
test_losses = []
test_counter = [i * len(train_loader.dataset) for i in range(n_epochs + 1)]


def train_model(epoch):
    print("Training model.")
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.item()))
            train_losses.append(loss.item())
            train_counter.append(
                (batch_idx * 64) + ((epoch - 1) * len(train_loader.dataset)))


def test_model():
    print("Testing model.")
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            test_loss += F.nll_loss(output, target, size_average=False).item()
            pred = output.data.max(1, keepdim=True)[1]
            correct += pred.eq(target.data.view_as(pred)).sum()
    test_loss /= len(test_loader.dataset)
    test_losses.append(test_loss)
    print('\nTest set: Avg. loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


def create_model():
    test_model()
    for epoch in range(1, n_epochs + 1):
        train_model(epoch)
        test_model()

    torch.save(model.state_dict(), './model.pt')


create_model()

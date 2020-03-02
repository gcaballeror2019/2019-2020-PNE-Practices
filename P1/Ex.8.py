from Seq1 import Seq


seq_list1 = Seq()
seq_list2 = Seq('ACTGA')
seq_list3 = Seq('ACDSFG')


print(f'Sequence 1:(Length: {seq_list1.len()}) {seq_list1} ')
print(f'Bases: {seq_list1.count()}')
print(f' Rev: {seq_list1.reverse()}')
print(f' Comp: {seq_list1.complement()}')

print(f'Sequence 2:(Length: {seq_list2.len()}) {seq_list2}')
print(f'Bases: {seq_list2.count()}')
print(f' Rev: {seq_list2.reverse()}')
print(f' Comp: {seq_list2.complement()}')

print(f'Sequence 3:(Length: {seq_list3.len()}) {seq_list3}')
print(f'Bases: {seq_list3.count()}')
print(f' Rev: {seq_list3.reverse()}')
print(f' Comp: {seq_list3.complement()}')

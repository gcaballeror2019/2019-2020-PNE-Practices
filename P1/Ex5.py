from Seq1 import Seq


seq_list1 = Seq()
seq_list2 = Seq('ACTGA')
seq_list3 = Seq('ACDSFG')


print(f'Sequence 1:(Length: {seq_list1.len()}) {seq_list1} ')
print(f'{seq_list1.count_base()}')
print(f'Sequence 2:(Length: {seq_list2.len()}) {seq_list2}')
print(f'{seq_list2.count_base()}')
print(f'Sequence 3:(Length: {seq_list3.len()}) {seq_list3}')
print(f'{seq_list3.count_base()}')

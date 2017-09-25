Requires:
Python-2.7
pandas
numpy

This code generates the representation of perturbations given the number of perturbations, initial abundance, fold coverage, number of doublings and number of splits

To run, type:
python representation_modeling_v1.0.py -n <Number of perturbations, default:100> -a <.txt file, no header, distribution to calculate initial abundance> -x <fold coverage, default:1000> -d <Number of doublings, default:3> -s <Number of splits, default=7>
